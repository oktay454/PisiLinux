#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcNAME()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGELOG.txt", "LICENSE.txt", "README.txt")
