import os
import pytest

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    "package_name", [
        "sudo",
    ]
)
def test_package_installed(host, package_name):
    pkg = host.package(package_name)

    assert pkg.is_installed


@pytest.mark.parametrize(
    "string, status", [
        ("sudo ALL=(ALL) NOPASSWD: ALL", True),
        ("devops ALL=NOPASSWD:/usr/bin/rsync", True),
        ('Defaults env_keep += "SSH_AUTH_SOCK"', True),
    ]
)
def test_configuration(host, string, status):
    with host.sudo():
        config = host.file('/etc/sudoers')

        assert config.exists
        assert config.contains(string) is status
