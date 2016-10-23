ansible-pip
===========
[![Build Status](https://travis-ci.org/futurice/ansible-pip.svg?branch=master)](https://travis-ci.org/futurice/ansible-pip)

Ansible role for [pip](https://pip.pypa.io/en/stable/). Installs pip, when not yet installed.

Requirements
------------


Role Variables
--------------


Dependencies
------------


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: futurice.pip }

License
-------

BSD
