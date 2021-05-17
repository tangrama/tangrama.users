import os
import pytest

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize(
    "group_name, status", [
        ("devops", True),
        ("sudo", True),
        ("developers", True),
        ("dummygroup", False),
    ]
)
def test_group_state(host, group_name, status):
    g = host.group(group_name)

    assert g.exists is status
