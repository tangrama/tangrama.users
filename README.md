# Tangrama: User Management

User & Group management role for Ubuntu servers.

This role is a wrapper for [User](https://docs.ansible.com/ansible/latest/modules/user_module.html) and [Group](https://docs.ansible.com/ansible/latest/modules/group_module.html).

## Role Variables

This role expects two global scope variables to be set: *user_groups*, *users*. Both variables should be dictionaries containing information about users and user groups to be managed.


### user_groups

Each pair of key, value describes a group in the system. Key will be mapped as the group name and in the values there should be a description of the group and the state of the group -- either *present* or *absent*.

Example with two groups to be added and one to be removed.

```yaml
    user_groups:
      devops:
        description: 'Devops Team'
        state: present
      developers:
        description: 'Developers'
        state: present
      dummy_group:
        description: 'Dummy Group'
        state: absent
```

### users

Each pair of key, value describes a user in the system. Key will be mapped as the user name and in the value a dictionary with user information should be passed:

* name: Fullname of the user.
* email: Email of the user.
* public_keys: List of SSH public keys.
* password: Password hash, created with plone/devops-mkpasswd docker image.
* update_password: When to update user password. Either *on_create* or *always*. Default: *on_create*.
* state: Either *present* or *absent*.
* shell: Shell to be used.
* groups: List of group names the user will be added to.

Example with three users, two to be added and one to be removed.

```yaml
    users:
      'guido':
        name: 'Guido van Rossum'
        email: 'bdfl@python.org'
        public_keys:
          - 'ssh-rsa...guido@abc.local'
        password: '$5$vIvCpGfkL.nGx7GB$6dfT9W8ad/Nk7VBWfQM6pBHHKceaOJozOaYPTBDRxn9'
        state: present
        shell: '/bin/bash'
        groups:
          - 'sudo'
          - 'devops'
      'dtremea':
        name: 'Dorneles Tremea'
        email: 'deo@plone.org'
        public_keys:
          - 'ssh-rsa...dtremea@plone.local'
        password: '$5$i5mvDOW67u1Z2Uv2$a6/CsZ1VXLRWVLGSYfcc48CW/s76NzUKU0zYsBnBqj.'
        state: present
        shell: '/bin/bash'
        groups:
          - 'developers'
      'larry':
        name: 'Larry Wall'
        email: 'larry@perl.org'
        state: absent
```

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: tangrama.users }

## Testing

This role uses [molecule](https://molecule.readthedocs.io/) for linting and testing.

```shell
    molecule test
```

## License

GPLv2

## Author Information

* Tangrama (tangrama at simplesconsultoria dot com dot br)

