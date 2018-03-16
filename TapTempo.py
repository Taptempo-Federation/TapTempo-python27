#!/usr/bin/python
# -*- coding: utf-8 -*
# #############################################################################
#    Copyright (C) 2018 manatlan manatlan[at]gmail(dot)com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 2 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# https://github.com/manatlan/reqman
# #############################################################################
#
# https://linuxfr.org/users/manatlan/journaux/portage-de-taptempo-en-python-2-7

import sys,termios,tty,datetime

def getKey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print "tapTempo : press any key (q for quit)"
t=[]
while getKey()!="q":
    t.append( datetime.datetime.now() )
    ll=[ (j-i).microseconds for i, j in zip(t[:-1], t[1:]) ][-5:]
    if ll: print "BPM:",60000000*len(ll)/sum(ll)

