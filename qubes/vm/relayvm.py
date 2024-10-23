# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2024 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import List
from qubes.vm.remotevm import RemoteVM
from qubes.vm.qubesvm import QubesVM



class LocalRelayVM(RemoteVM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forward_rpc: str = ""


class RelayVM(RemoteVM):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exposed_qubes: List[RemoteVM] = []
