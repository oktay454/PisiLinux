#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DWITH_ASF=On -DWITH_MP4=On")

def build():
    cmaketools.make()

def install():
   cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

   pisitools.dodoc("AUTHORS","COPYING*")
