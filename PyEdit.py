import textConfig

Version = 2.1
import sys, os
from tkinter import *
from tkinter.filedialog import Open, SaveAs
from tkinter.messagebox import showinfo, showerror, askyesno
from tkinter.simpledialog import askstring, askinteger
from tkinter.colorchooser import askcolor
from PP4E.Gui.Tools.guimaker import *

try:
    import PP4E.textConfig

    configs = textConfig.__dict__

except:
    configs = {}

helpText = f"""
PyEdit
Version = {Version}

by Mark Lutz
"""

START = '1.0'
SEL_FIRST = SEL + '.first'
SEL_LAST = SEL + '.last'

FontScale = 0
if sys.platform[:3] != 'win':
    FontScale = 3


class PyEdit:
    startfildir = '.'
    editwindows = []



    if __name__ == '__main__':
        from PP4E
