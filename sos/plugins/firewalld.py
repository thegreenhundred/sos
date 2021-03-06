# Copyright (C) 2014 Red Hat, Inc. Jamie Bainbridge <jbainbri@redhat.com>
# Copyright (C) 2014 Red Hat, Inc. Bryn M. Reeves <bmr@redhat.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin


class FirewallD(Plugin, RedHatPlugin):
    """Firewall daemon
    """

    plugin_name = 'firewalld'
    profiles = ('network',)

    packages = ('firewalld',)

    def setup(self):
        self.add_copy_spec([
            "/etc/firewalld/firewalld.conf",
            "/etc/firewalld/*.xml",
            "/etc/firewalld/icmptypes/*.xml",
            "/etc/firewalld/services/*.xml",
            "/etc/firewalld/zones/*.xml",
            "/etc/sysconfig/firewalld"
        ])

        # use a 10s timeout to workaround dbus problems in
        # docker containers.
        self.add_cmd_output([
            "firewall-cmd --list-all-zones",
            "firewall-cmd --permanent --list-all-zones"
        ], timeout=10)

# vim: set et ts=4 sw=4 :
