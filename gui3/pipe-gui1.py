# GUI reader side: route spawned program standard output to a GUI window

from gui_redirect_stream import redirectedGuiShellCmd       # uses GuiOutput
redirectedGuiShellCmd('python -u pipe-nongui.py')                 # -u: unbuffered
