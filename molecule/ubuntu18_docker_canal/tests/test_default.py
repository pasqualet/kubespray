import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_service(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled

def test_etcd_service(host):
    etcd = host.service("etcd")
    assert etcd.is_running
    assert etcd.is_enabled
