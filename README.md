# pew

[![Build Status](https://travis-ci.org/Temelio/ansible-role-pew.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-pew)

Install pew package.

Today, only globally pip install is available, but you're free to open PR for new installation methods or OS support.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Package management
pew_apt_update_cache: True
pew_apt_cache_valid_time: 3600
pew_system_dependencies: "{{ _pew_system_dependencies | default([]) }}"
pew_pip_packages:
  - name: 'pew'
    version: '1.1.2'

# Install method
# * pip: use python packages on pypi
pew_install_method: 'pip'
pew_install_globally: True
pew_manage_system_dependencies: True
```

### Debian OS family role variables

``` yaml
_pew_system_dependencies:
  - name: 'git'
  - name: 'python-pip'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.pew }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
