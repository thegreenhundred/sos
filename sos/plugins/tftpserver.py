# Copyright (C) 2007 Shijoe George <spanjikk@redhat.com>

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


class TftpServer(Plugin, RedHatPlugin):
    """TFTP server
    """

    plugin_name = 'tftpserver'
    profiles = ('sysmgmt', 'network')

    files = ('/etc/xinetd.d/tftp',)
    packages = ('tftp-server',)

    def setup(self):
        self.add_cmd_output("ls -lanR /tftpboot")

# vim: set et ts=4 sw=4 :
