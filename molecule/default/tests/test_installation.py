"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('git'),
    ('python-pip'),
])
def test_system_packages(host, name):
    """
    Ensure system packages installed
    """

    assert host.package(name).is_installed


@pytest.mark.parametrize('name', [
    ('pew'),
])
def test_pip_packages(host, name):
    """
    Ensure Pip packages installed
    """

    assert name in host.pip_package.get_packages()
