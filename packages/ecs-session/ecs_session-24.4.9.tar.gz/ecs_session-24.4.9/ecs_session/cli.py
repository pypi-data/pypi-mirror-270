#!/usr/bin/env python3
"""
ecs-session cli program
"""

import configargparse
import shtab
from boto3 import session
from simple_term_menu import TerminalMenu

from ecs_session import ECSSession


def get_parser():
    """argument parser"""
    parser = configargparse.ArgParser(
        prog="ecs-session",
        auto_env_var_prefix="ECS_SESSION_",
    )
    shtab.add_argument_to(
        parser,
        ["--print-completion"],
        help="Print shell-completion. Run '. <(ecs-session --print-completion)' to load.",
    )
    parser.add_argument("--profile", help="AWS Profile", default="default")
    parser.add_argument(
        "--region",
        help="AWS region name",
        default="eu-central-1",
    )
    parser.add_argument(
        "--cluster",
        help="ECS cluster name",
    )
    parser.add_argument(
        "--service",
        help="ECS service name",
    )
    parser.add_argument(
        "--task",
        help="ECS task id",
    )
    parser.add_argument(
        "--container",
        help="ECS container name",
    )
    parser.add_argument(
        "--command",
        help="Execute command",
        default="/bin/bash",
    )
    parser.add_argument(
        "--remote-port",
        help="ECS container remote port",
        type=int,
    )
    parser.add_argument(
        "--local-port",
        help="Local port for forwarding. Defaults to random port (0)",
        type=int,
        default=0,
    )
    subparsers = parser.add_subparsers(
        dest="action",
        help="action",
    )
    subparsers.required = True
    subparsers.add_parser("forward", help="Portforwarding")
    subparsers.add_parser("command", help="Execute command")
    return parser


def show_menu(items: list, title: str, source: list = None, back: bool = True):
    """
    menu function
    """
    index = None
    source = source or items
    if back:
        items = items + ["Back"]
    menu = TerminalMenu(
        items,
        title=f'? {title} (Press "q"/"ESC" to quit):\n',
        show_search_hint=True,
    )
    index = menu.show()
    if items[index] == "Back":
        return None, index
    if index is None:
        exit(0)
    return source[index], index


def ecs_paginator(ecs: session.Session.client, paginator: str, leaf: str, **kwargs):
    """
    aws paginator
    """
    arns = []
    paginator = ecs.get_paginator(paginator)
    iterator = paginator.paginate(**kwargs)
    for page in iterator:
        arns.extend(page.get(leaf))
    return arns


def get_cluster(ecs: session.Session.client, cluster: str):
    """
    get clusters
    """
    if cluster:
        return cluster, None
    arns = ecs_paginator(
        ecs=ecs,
        paginator="list_clusters",
        leaf="clusterArns",
    )
    clusters = [cluster.split("/")[-1] for cluster in arns]
    return show_menu(
        items=clusters,
        title="Select cluster",
        back=False,
    )


def get_service(ecs: session.Session.client, service: str, cluster: str):
    """
    get service
    """
    if not cluster:
        return cluster, None, None
    if service:
        return cluster, service, None
    arns = ecs_paginator(
        ecs=ecs,
        paginator="list_services",
        leaf="serviceArns",
        cluster=cluster,
    )
    services = [service.split("/")[-1] for service in arns]
    ret = show_menu(
        items=services,
        title=f"[{cluster}] Select service",
    )
    if ret[0] is None:
        return (None, *ret)
    return (cluster, *ret)


def get_task(ecs: session.Session.client, task: str, cluster: str, service: str):
    """
    get services
    """
    if not service:
        return cluster, service, None, None
    if task:
        return cluster, service, task, None
    arns = ecs_paginator(
        ecs=ecs,
        paginator="list_tasks",
        leaf="taskArns",
        cluster=cluster,
        serviceName=service,
    )
    tasks = [task.split("/")[-1] for task in arns]
    ret = show_menu(
        items=tasks,
        title=f"[{cluster}|{service}] Select task",
    )
    if ret[0] is None:
        return (cluster, None, *ret)
    return (cluster, service, *ret)


def get_container(cluster: str, service: str, task: str, containers: list, container: str):
    """
    get container
    """
    if container:
        return container, containers.index(container)
    ret = show_menu(
        items=containers,
        title=f"[{cluster}|{service}|{task}] Select container",
    )
    if ret[0] is None:
        return (None, *ret)
    return (task, *ret)


def run():
    """main cli function"""
    parser = get_parser()
    arguments = parser.parse_args()
    boto3_session_args = {
        "region_name": arguments.region,
    }
    if arguments.profile != "default":
        boto3_session_args.update({"profile_name": arguments.profile})
    boto3_session = session.Session(**boto3_session_args)
    ecs = boto3_session.client("ecs")
    ssm = boto3_session.client("ssm")
    cluster, service, task, container = (arguments.cluster, arguments.service, arguments.task, arguments.container)
    while not (cluster and service and task and container):
        cluster, _ = get_cluster(ecs=ecs, cluster=cluster)
        cluster, service, _ = get_service(ecs=ecs, cluster=cluster, service=service)
        cluster, service, task, _ = get_task(ecs=ecs, cluster=cluster, service=service, task=task)
        if cluster and task:
            task_details = ecs.describe_tasks(cluster=cluster, tasks=[task])
            containers = [container.get("name") for container in task_details.get("tasks")[0].get("containers")]
            task, container, container_index = get_container(
                cluster=cluster,
                service=service,
                task=task,
                containers=containers,
                container=container,
            )
    remote_port = arguments.remote_port
    if arguments.action == "forward" and not remote_port:
        task_definition_arn = task_details.get("tasks")[0].get("taskDefinitionArn")
        task_definition = ecs.describe_task_definition(taskDefinition=task_definition_arn).get("taskDefinition")
        ports = [
            str(container.get("containerPort"))
            for container in task_definition.get("containerDefinitions")[container_index].get("portMappings")
        ]
        remote_port, _ = show_menu(items=ports, title="Select port")
    ecs_session = ECSSession(
        cluster=cluster,
        command=arguments.command,
        container=container,
        container_index=container_index,
        ecs=ecs,
        local_port=arguments.local_port,
        profile=arguments.profile,
        region=arguments.region,
        remote_port=remote_port,
        ssm=ssm,
        task=task,
        task_details=task_details,
    )
    function = {
        "forward": ecs_session.port_forward,
        "command": ecs_session.execute_command,
    }
    print("---")
    print(f"cluster: {cluster}")
    print(f"service: {service}")
    print(f"task: {task}")
    print(f"container: {container}")
    print("---")
    function.get(arguments.action)()
