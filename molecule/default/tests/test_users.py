import os
import pytest

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    "user_name, status", [
        ("guido", True),
        ("dtremea", True),
        ("larry", False)
    ]
)
def test_user_state(host, user_name, status):
    u = host.user(user_name)

    assert u.exists is status


@pytest.mark.parametrize(
    "user_name, shell, groups", [
        ("guido", "/bin/bash", ["devops", "sudo"]),
        ("dtremea", "/bin/bash", ["developers", ]),
    ]
)
def test_user_properties(host, user_name, shell, groups):
    u = host.user(user_name)

    assert u.shell == shell
    for group in groups:
        assert group in u.groups


@pytest.mark.parametrize(
    "user_name, keys", [
        ("guido", 1),
        ("dtremea", 2),
    ]
)
def test_user_ssh_keys(host, user_name, keys):
    with host.sudo():
        config = host.file(f"/home/{user_name}/.ssh/authorized_keys")
        lines = [line for line in config.content.split(b"\n") if line]
        assert config.exists
        assert config.user == user_name
        assert len(lines) == keys
