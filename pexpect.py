import sys
import time

import boto3

import pexpect
import pexpect.expect
import pexpect.replwrap



def spawn_session(container, family, cluster, ecs_client):
    print(f'Spawning Session: {container}, {family}, {cluster}')
    rsp = ecs_client.list_tasks(cluster=cluster, family=family)
    print(rsp)
    task_arn = rsp.get('taskArns')[0]
    local_argv = [
        'aws', 'ecs', 'execute-command',
        '--command', '/bin/bash',
        '--interactive', '--task', task_arn, '--container', container,
        '--cluster', cluster
    ]
    ps = pexpect.spawn(' '.join(local_argv), timeout=900, logfile=sys.stdout.buffer)
    ps.expect('ecs-execute-command.*# ', timeout=15)

    return ps

def repl_session_example(container, family, cluster, ecs_client):
    rsp = ecs_client.list_tasks(cluster=cluster, family=family)
    print(rsp)
    task_arn = rsp.get('taskArns')[0]
    # bash = pexpect.replwrap.bash()
    local_argv = [
        'aws', 'ecs', 'execute-command',
        '--command', '/bin/bash',
        '--interactive', '--task', task_arn, '--container', container,
        '--cluster', cluster
    ]
    bash = pexpect.replwrap.REPLWrapper(' '.join(local_argv), '#', None)

    return bash

def bash_session_example(container, family, cluster, ecs_client):
    rsp = ecs_client.list_tasks(cluster=cluster, family=family)
    print(rsp)
    task_arn = rsp.get('taskArns')[0]
    local_argv = [
        'aws', 'ecs', 'execute-command',
        '--command', '/bin/bash',
        '--interactive', '--task', task_arn, '--container', container,
        '--cluster', cluster
    ]
    bash = pexpect.replwrap.bash()
    bash.run_command(' '.join(local_argv))

    return bash


if __name__ == '__main__':
    ecs = boto3.client('ecs')   
    container = 'CONTAINER'
    family = 'TASK_FAMILY'
    cluster = 'CLUSTER_ARN'
    # bash = repl_session_example(container, family, cluster, ecs)
    # bash = bash_session_example(container, family, cluster, ecs)
    bash = spawn_session(container, family, cluster, ecs)
    for cmd in ['pwd', 'python --version', 'sleep 5', 'echo 2']:
        # print(f'Sending: {cmd}')
        bash.sendline(cmd)
        bash.expect('# ')
        # print(f'before: {bash.before}')
        # print(f'after: {bash.after}')
        # out = bash.run_command(cmd)
        # print(out)
    pass
