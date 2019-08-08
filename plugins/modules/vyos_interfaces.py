#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for vyos_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: vyos_interfaces
version_added: 2.9
short_description: Manages interface attributes of VyOS network devices.
description:
  - This module manages the interface attributes on VyOS network devices.
  - This module supports managing base attributes of Ethernet, Bonding,
    VXLAN, Loopback and Virtual Tunnel Interfaces.
author: Nilashish Chakraborty (@nilashishc)
options:
  config:
    description: The provided interfaces configuration.
    type: list
    suboptions:
      name:
        description:
        - Full name of the interface, e.g. eth0, eth1, bond0, vti1, vxlan2.
        type: str
        required: True
      description:
        description:
          - Interface description.
        type: str
      duplex:
        description:
          - Interface duplex mode.
          - Applicable for Ethernet interfaces only.
        choices: ['full', 'half', 'auto']
        type: str
      enabled:
        default: True
        description:
          - Administrative state of the interface.
          - Set the value to C(true) to administratively enable
            the interface or C(false) to disable it.
        type: bool
      mtu:
        description:
          - MTU for a specific interface. Refer to vendor documentation for valid values.
          - Applicable for Ethernet, Bonding, VXLAN and Virtual Tunnel interfaces.
        type: int
      speed:
        description:
          - Interface link speed.
          - Applicable for Ethernet interfaces only.
        type: str
        choices: ['auto', '10', '100', '1000', '2500', '10000']
      vifs:
        description:
          - Virtual sub-interfaces related configuration.
          - 802.1Q VLAN interfaces are represented as virtual sub-interfaces in VyOS.
        type: list
        suboptions:
          vlan_id:
            description:
              - Identifier for the virtual sub-interface.
            type: int
          description:
            description:
              - Virtual sub-interface description.
            type: str
          enabled:
            description:
              - Administrative state of the virtual sub-interface.
              - Set the value to C(true) to administratively enable
                the interface or C(false) to disable it.
            type: bool
            default: True
          mtu:
            description:
              - MTU for the virtual sub-interface.
              - Refer to vendor documentation for valid values.
            type: int
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged
#
# -------------
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo

- name: Merge provided configuration with device configuration
  vyos_interfaces:
    config:
      - name: eth2
        description: 'Configured by Ansible'
        enabled: True
        vifs:
          - vlan_id: 200
            description: "VIF 200 - ETH2"

      - name: eth3
        description: 'Configured by Ansible'
        mtu: 1500

      - name: bond1
        description: 'Bond - 1'
        mtu: 1200

      - name: vti2
        description: 'VTI - 2'
        enabled: false
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#      	{
#            "enabled": true,
#            "name": "lo"
#      	},
#       {
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "enabled": true,
#            "name": "eth2"
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "set interfaces ethernet eth2 description 'Configured by Ansible'",
#        "set interfaces ethernet eth2 vif 200",
#        "set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'",
#        "set interfaces ethernet eth3 description 'Configured by Ansible'",
#        "set interfaces ethernet eth3 mtu '1500'",
#        "set interfaces bonding bond1",
#        "set interfaces bonding bond1 description 'Bond - 1'",
#        "set interfaces bonding bond1 mtu '1200'",
#        "set interfaces vti vti2",
#        "set interfaces vti vti2 description 'VTI - 2'",
#        "set interfaces vti vti2 disable"
#    ]
#
# "after": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1200,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "VTI - 2",
#            "enabled": false,
#            "name": "vti2"
#        },
#        {
#            "description": "Configured by Ansible",
#            "enabled": true,
#            "mtu": 1500,
#            "name": "eth3"
#        },
#        {
#            "description": "Configured by Ansible",
#            "enabled": true,
#            "name": "eth2",
#            "vifs": [
#                {
#                    "description": "VIF 200 - ETH2",
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# -------------
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1200'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'
# set interfaces ethernet eth3 description 'Configured by Ansible'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 mtu '1500'
# set interfaces loopback lo
# set interfaces vti vti2 description 'VTI - 2'
# set interfaces vti vti2 disable
#


# Using replaced
#
# -------------
# Before state:
# -------------
#
# vyos:~$ show configuration commands | grep eth
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1400'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 description 'Management Interface for the Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:f3:6c:b5'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Eng Team'
# set interfaces ethernet eth1 duplex 'full'
# set interfaces ethernet eth1 hw-id '08:00:27:ad:ef:65'
# set interfaces ethernet eth1 smp_affinity 'auto'
# set interfaces ethernet eth1 speed '100'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 duplex 'full'
# set interfaces ethernet eth2 hw-id '08:00:27:ab:4e:79'
# set interfaces ethernet eth2 mtu '500'
# set interfaces ethernet eth2 smp_affinity 'auto'
# set interfaces ethernet eth2 speed '100'
# set interfaces ethernet eth2 vif 200 description 'Configured by Ansible'
# set interfaces ethernet eth3 description 'Configured by Ansible'
# set interfaces ethernet eth3 duplex 'full'
# set interfaces ethernet eth3 hw-id '08:00:27:17:3c:85'
# set interfaces ethernet eth3 mtu '1500'
# set interfaces ethernet eth3 smp_affinity 'auto'
# set interfaces ethernet eth3 speed '100'
# set interfaces loopback lo
#
#
- name: Replace device configurations of listed interfaces with provided configurations
  vyos_interfaces:
    config:
      - name: eth2
        description: "Replaced by Ansible"

      - name: eth3
        description: "Replaced by Ansible"

      - name: eth1
        description: "Replaced by Ansible"
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
#
# "before": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1400,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": true,
#            "mtu": 1500,
#            "name": "eth3",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": true,
#            "mtu": 500,
#            "name": "eth2",
#            "speed": "100",
#            "vifs": [
#                {
#                    "description": "VIF 200 - ETH2",
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "description": "Configured by Ansible Eng Team",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth1",
#            "speed": "100"
#        },
#        {
#            "description": "Management Interface for the Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces ethernet eth2 speed",
#        "delete interfaces ethernet eth2 duplex",
#        "delete interfaces ethernet eth2 mtu",
#        "delete interfaces ethernet eth2 vif 200 description",
#        "set interfaces ethernet eth2 description 'Replaced by Ansible'",
#        "delete interfaces ethernet eth3 speed",
#        "delete interfaces ethernet eth3 duplex",
#        "delete interfaces ethernet eth3 mtu",
#        "set interfaces ethernet eth3 description 'Replaced by Ansible'",
#        "delete interfaces ethernet eth1 speed",
#        "delete interfaces ethernet eth1 duplex",
#        "set interfaces ethernet eth1 description 'Replaced by Ansible'"
#    ]
#
# "after": [
#        {
#            "description": "Bond - 1",
#            "enabled": true,
#            "mtu": 1400,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth2",
#            "vifs": [
#                {
#                    "enabled": true,
#                    "vlan_id": "200"
#                }
#            ]
#        },
#        {
#            "description": "Replaced by Ansible",
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "description": "Management Interface for the Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# -------------
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond1 description 'Bond - 1'
# set interfaces bonding bond1 mtu '1400'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Management Interface for the Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Replaced by Ansible'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 description 'Replaced by Ansible'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 vif 200
# set interfaces ethernet eth3 description 'Replaced by Ansible'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
#
#
# Using overridden
#
#
# --------------
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Ethernet Interface - 0'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 mtu '1200'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Eng Team'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 mtu '100'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 vif 100 description 'VIF 100 - ETH1'
# set interfaces ethernet eth1 vif 100 disable
# set interfaces ethernet eth2 description 'Configured by Ansible Team (Admin Down)'
# set interfaces ethernet eth2 disable
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 mtu '600'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 description 'Configured by Ansible Network'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
# set interfaces vti vti1 description 'Virtual Tunnel Interface - 1'
# set interfaces vti vti1 mtu '68'
#
#
- name: Overrides all device configuration with provided configuration
  vyos_interfaces:
    config:
      - name: eth0
        description: Outbound Interface For The Appliance
        speed: auto
        duplex: auto

      - name: eth2
        speed: auto
        duplex: auto

      - name: eth3
        mtu: 1200
    state: overridden
#
#
# ------------------------
# Module Execution Result
# ------------------------
#
# "before": [
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Virtual Tunnel Interface - 1",
#            "enabled": true,
#            "mtu": 68,
#            "name": "vti1"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "description": "Configured by Ansible Team (Admin Down)",
#            "enabled": false,
#            "mtu": 600,
#            "name": "eth2"
#        },
#        {
#            "description": "Configured by Ansible Eng Team",
#            "enabled": true,
#            "mtu": 100,
#            "name": "eth1",
#            "vifs": [
#                {
#                    "description": "VIF 100 - ETH1",
#                    "enabled": false,
#                    "vlan_id": "100"
#                }
#            ]
#        },
#        {
#            "description": "Ethernet Interface - 0",
#            "duplex": "auto",
#            "enabled": true,
#            "mtu": 1200,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces vti vti1 description",
#        "delete interfaces vti vti1 mtu",
#        "delete interfaces ethernet eth1 description",
#        "delete interfaces ethernet eth1 mtu",
#        "delete interfaces ethernet eth1 vif 100 description",
#        "delete interfaces ethernet eth1 vif 100 disable",
#        "delete interfaces ethernet eth0 mtu",
#        "set interfaces ethernet eth0 description 'Outbound Interface For The Appliance'",
#        "delete interfaces ethernet eth2 description",
#        "delete interfaces ethernet eth2 mtu",
#        "set interfaces ethernet eth2 duplex 'auto'",
#        "delete interfaces ethernet eth2 disable",
#        "set interfaces ethernet eth2 speed 'auto'",
#        "delete interfaces ethernet eth3 description",
#        "set interfaces ethernet eth3 mtu '1200'"
#    ],
#
# "after": [
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "enabled": true,
#            "name": "vti1"
#        },
#        {
#            "enabled": true,
#            "mtu": 1200,
#            "name": "eth3"
#        },
#        {
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth2",
#            "speed": "auto"
#        },
#        {
#            "enabled": true,
#            "name": "eth1",
#            "vifs": [
#                {
#                    "enabled": true,
#                    "vlan_id": "100"
#                }
#            ]
#        },
#        {
#            "description": "Outbound Interface For The Appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# ------------
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface For The Appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 vif 100
# set interfaces ethernet eth2 duplex 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 speed 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 mtu '1200'
# set interfaces loopback lo
# set interfaces vti vti1
#
#
# Using deleted
#
#
# -------------
# Before state
# -------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond0 mtu '1300'
# set interfaces bonding bond1 description 'LAG - 1'
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface for this appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 description 'Configured by Ansible Network'
# set interfaces ethernet eth1 duplex 'full'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth1 speed '100'
# set interfaces ethernet eth2 description 'Configured by Ansible'
# set interfaces ethernet eth2 disable
# set interfaces ethernet eth2 duplex 'full'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 mtu '600'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth2 speed '100'
# set interfaces ethernet eth3 description 'Configured by Ansible Network'
# set interfaces ethernet eth3 duplex 'full'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 speed '100'
# set interfaces loopback lo
#
#
- name: Delete attributes of given interfaces (Note - This won't delete the interfaces themselves)
  vyos_interfaces:
    config:
      - name: bond1

      - name: eth1

      - name: eth2

      - name: eth3
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
# "before": [
#        {
#            "enabled": true,
#            "mtu": 1300,
#            "name": "bond0"
#        },
#        {
#            "description": "LAG - 1",
#            "enabled": true,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth3",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible",
#            "duplex": "full",
#            "enabled": false,
#            "mtu": 600,
#            "name": "eth2",
#            "speed": "100"
#        },
#        {
#            "description": "Configured by Ansible Network",
#            "duplex": "full",
#            "enabled": true,
#            "name": "eth1",
#            "speed": "100"
#        },
#        {
#            "description": "Outbound Interface for this appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
# "commands": [
#        "delete interfaces bonding bond1 description",
#        "delete interfaces ethernet eth1 speed",
#        "delete interfaces ethernet eth1 duplex",
#        "delete interfaces ethernet eth1 description",
#        "delete interfaces ethernet eth2 speed",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 duplex",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 description",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth2 mtu",
#        "delete interfaces ethernet eth2 disable",
#        "delete interfaces ethernet eth3 speed",
#        "delete interfaces ethernet eth3 duplex",
#        "delete interfaces ethernet eth3 description"
#    ]
#
# "after": [
#        {
#            "enabled": true,
#            "mtu": 1300,
#            "name": "bond0"
#        },
#        {
#            "enabled": true,
#            "name": "bond1"
#        },
#        {
#            "enabled": true,
#            "name": "lo"
#        },
#        {
#            "enabled": true,
#            "name": "eth3"
#        },
#        {
#            "enabled": true,
#            "name": "eth2"
#        },
#        {
#            "enabled": true,
#            "name": "eth1"
#        },
#        {
#            "description": "Outbound Interface for this appliance",
#            "duplex": "auto",
#            "enabled": true,
#            "name": "eth0",
#            "speed": "auto"
#        }
#    ]
#
#
# ------------
# After state
# ------------
#
# vyos@vyos:~$ show configuration commands | grep interfaces
# set interfaces bonding bond0 mtu '1300'
# set interfaces bonding bond1
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 description 'Outbound Interface for this appliance'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
# set interfaces ethernet eth1 smp-affinity 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth2 smp-affinity 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces loopback lo
#
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - 'set interfaces ethernet eth1 mtu 1200'
    - 'set interfaces ethernet eth2 vif 100 description VIF 100'
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.interfaces.interfaces import InterfacesArgs
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.interfaces.interfaces import Interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=InterfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
