#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

WorkDir = "./"

def install():
    pisitools.insinto("%s/kdm/themes/" % kde4.appsdir, "kdm-theme-pardus", "pardus")

