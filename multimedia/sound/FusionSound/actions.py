#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "core/FusionSound.git/"
KeepSpecial = ["libtool"]

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.rename("/usr/bin/fsdump", "FusionSound-dump")
    pisitools.remove("/usr/lib/*.la")

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("AUTHORS")
