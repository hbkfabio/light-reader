#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


from gi.repository import Gtk
from  utiles import define_signals, define_widgets


class MainReader():
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('./ui/main.glade')
        define_widgets(self, self.builder)
        define_signals(self, self.builder, 'wnMain')
        self.builder.connect_signals(self)
        self.wnMain.maximize()
        self.wnMain.show_all()

    def on_delete_event(self, widget, event):
        Gtk.main_quit()

if __name__ == '__main__':
    m = MainReader()
    Gtk.main()

