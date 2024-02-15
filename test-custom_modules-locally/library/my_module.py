#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def size_to_human(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(size) < 1024.0:
            return "%3.1f %s" % (size, unit)
        size /= 1024.0
    return "%3.1f %s" % (size, 'PB')

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        name=dict(type='str', required=True),
        path=dict(type='str', required=True),
        to_human=dict(type='bool', required=False, default=False)
    )

    result = dict(
        dir_name='',
        size_dir='',
        human_rd=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )


    if module.check_mode:
        module.exit_json(**result)
        
    result['dir_name'] = module.params['path']
    
    s = get_size(module.params['path'])
    result['size_dir'] = s
    if module.params['to_human']:
        
        result['human_rd'] = size_to_human(s)

    if module.params['path'] == '':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()