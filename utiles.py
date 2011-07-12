from gi.repository import  Gtk

wins = {}
def add_tab(self, widget, label, ntb):
    p = -1
    if not self.wins.has_key(label):
       l = Gtk.Label('')
       l.set_text_with_mnemonic(label)
       ntb.append_page(widget, l)
#       widget.show()
       self.wins[label] = (widget, len(self.wins))
    else:
       ntb.show_all()
       ntb.set_current_page(self.wins[label][1])
       a = ntb.get_current_page()
    p = len(self.wins) - 1
    ntb.set_current_page(-1)

    return 

def remove_tab(self, label, ntb):
    ntb.remove(self.wins[label][0])
    del self.wins[label]
    return

def define_widgets(self, builder):
    for widget in builder.get_objects():
        try:
            setattr(self, Gtk.Buildable.get_name(widget), widget)
        except:
            pass

def define_signals(self, builder, window):
    for widget in builder.get_objects():
        if type(widget) == type(Gtk.Dialog()):
            widget.connect("delete-event", self.on_delete_event)
        if type(widget) == type(Gtk.Window()):
            if Gtk.Buildable.get_name(widget) == window:
                widget.connect("delete-event", self.on_delete_event)
