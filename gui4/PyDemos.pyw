
import sys, time, os, glob, launchmodes
from tkinter import *

# -live loads root pages from server so CGIs run, -file loads local files
InternetMode = '-live'

################################################################################
# start building main GUI windows
################################################################################

from windows import MainWindow    # a Tk with icon, title, quit
from windows import PopupWindow   # same but Toplevel, diff quit
Root = MainWindow('PP4E Demos 2.1')

# build message window
Stat = PopupWindow('PP4E demo info')
Stat.protocol('WM_DELETE_WINDOW', lambda:0)      # ignore wm delete

Info = Label(Stat, text = 'Select demo',
             font=('courier', 20, 'italic'), padx=12, pady=12, bg='lightblue')
Info.pack(expand=YES, fill=BOTH)

################################################################################
# add launcher buttons with callback objects
################################################################################

from textEditor import TextEditorMainPopup

# demo launcher class
class Launcher(launchmodes.PortableLauncher):    # use wrapped launcher class
    def announce(self, text):                    # customize to set GUI label
        Info.config(text=text)

def viewer(sources):
    for filename in sources:
        TextEditorMainPopup(Root, filename,      # as pop up in this process
                            loadEncode='utf-8')  # else PyEdit may ask each!

def demoButton(name, what, doit, code, launcher=Launcher):
    """
    add buttons that runs doit command-line, and open all files in code;
    doit button retains state in an object, code in an enclosing scope;
    """
    rowfrm = Frame(Root)
    rowfrm.pack(side=TOP, expand=YES, fill=BOTH)

    b = Button(rowfrm, bg='navy', fg='white', relief=RIDGE, border=4)
    b.config(text=name, width=20, command=launcher(what, doit))
    b.pack(side=LEFT, expand=YES, fill=BOTH)

    b = Button(rowfrm, bg='beige', fg='navy')
    b.config(text='code', command=(lambda: viewer(code)))
    b.pack(side=LEFT, fill=BOTH)

# some imported module source files could be determined
# but we can't know where to stop on the import chains

################################################################################
# tkinter GUI demos - some use network connections
################################################################################

demoButton(name='PyEdit',
           what='Text file editor',                            # edit myself
           doit='textEditor.py PyDemos.pyw',    # assume in cwd
           code=['launchmodes.py',
                 'find.py',
                 'scrolledlist.py',          # show in PyEdit viewer        
                 'formrows.py',          # last = top of stacking
                 'guimaker.py',
                 'textConfig.py',
                 'textEditor.py'])

demoButton(name='PyView',
           what='Image slideshow, plus note editor',
           doit='slideShowPlus.py /gifs',
           code=['textEditor.py',
                 'slideShow.py',
                 'slideShowPlus.py'])

demoButton(name='PyDraw',
           what='Draw and move graphics objects',
           doit='movingpics.py /gifs',
           code=['movingpics_threads.py',
                 'movingpics_after.py',
                 'movingpics.py'])

demoButton(name='PyTree',
           what='Tree data structure viewer',
           doit='treeview.py',
           code=['parser2.py',
                 'btree.py',
                 'treeview_wrappers.py',
                 'treeview.py'])

demoButton(name='PyClock',
           what='Analog/digital clocks',
           doit='clockStyles.py gifs',
           code=['windows.py',
                 'clockStyles.py',
                 'clock.py'])

demoButton(name='PyToe',
           what='Tic-tac-toe game (AI)',
           doit='tictactoe.py',
           code=['tictactoe_lists.py',
                 'tictactoe.py'])

demoButton(name='PyForm',                              # view in-memory dict
           what='Persistent table viewer/editor',      # or cwd shelve of class
           doit='formgui.py',       # 0=do not reinit shelve
          #doit='Dbase/TableBrowser/formtable.py  shelve 0 pyformData-1.5.2',
          #doit='Dbase/TableBrowser/formtable.py  shelve 1 pyformData',
           code=['formtable.py',
                 'formgui.py'])

demoButton(name='PyCalc',
           what='Calculator, plus extensions',
           doit='calculator_plusplus.py',
           code=['calculator_plusplus.py',
                 'calculator_plus_ext.py',
                 'calculator_plus_emb.py',
                 'calculator.py'])

demoButton(name='PyFtp',
           what='Python+Tk ftp clients',
           doit='PyFtpGui.pyw',
           code=['form.py',
                 'putfile.py',
                 'getfile.py',
                 'putfilegui.py',
                 'getfilegui.py',
                 'PyFtpGui.pyw'])

# caveat: PyPhoto requires PIL to be installed: show note
demoButton(name='PyPhoto',
           what='PIL thumbnail image viewer',
           doit='pyphoto1.py /images',     # script, image dir
           code=['viewer_thumbs.py',
                 'pyphoto1.py',
                 'PyDemos-pil-note.txt'])

# get pymailgui source files by globbing
locat  = 'Internet/Email'
locat2 = locat + '/PyMailGui'

saved  = '%s/SavedMail/savemany-3E.txt' % locat2   # skip savefew-3E
saved += ' %s/SavedMail/i18n-4E %s/SavedMail/version30-4E' % (locat2, locat2)

source = glob.glob(locat + '/mailtools/*.py')   # N source files here + __init__
source+= glob.glob(locat + '/PyMailGui/*.py')   # M source files here + __init__
source+= glob.glob(locat + '/PyMailGui/*.html') # html help file in 2.1
source = [F for F in source if not (
                      os.path.basename(F)[0] == '_' and 
                      os.path.basename(F)[:2] != '__')]  # del tests

demoButton(name='PyMailGUI',
           what='Python+Tk pop/smtp email client',         # open on save files
           doit='%s/PyMailGui.py %s' % (locat2, saved),
           code=(['textEditor.py',          # lots of sourcecode!
                  'windows.py',
                  'threadtools.py'] + source) )

################################################################################
# web-based demos - PyInternet opens many smaller demos
################################################################################

# get pymailcgi source files - not incl mailtools!
pagepath = os.getcwd() + '/Internet/Web'
pymailcgifiles = (glob.glob('Internet/Web/PyMailCgi/cgi-bin/*.py') +  # 11 .py
                  ['Internet/Web/PyMailCgi/pymailcgi.html'])          # +root
                                                                      # +server?
if InternetMode == '-file':
    demoButton('PyMailCGI',
               'Browser-based pop/smtp email interface',
               'LaunchBrowser.pyw -file %s/PyMailCgi/pymailcgi.html' % pagepath,
               pymailcgifiles)

    demoButton('PyInternet',
               'Internet-based demo launcher page',
               'LaunchBrowser.pyw -file %s/PyInternetDemos.html' % pagepath,
               ['%s/PyInternetDemos.html' % pagepath]) 

else:
    web80_started = web8000_started = False

    def startLocalWebServers(port):
        """
        on Windows succeeds silently if server already listening
        on the port; caveat: should only run 1 server per port;
        global per-process flag won't fix: the servers live on;

        4E: specialized to use StartArgs on Windows which spawns
        in parallel, seems to work more reliably, and pops up a 
        command prompt shell window to make it more obvious that 
        a server is running and trace its status; also enhanced to
        start a web server only on first select of demo's button;
        """
        global web80_started, web8000_started
        onWin   = sys.platform.startswith('win')
        spawner = launchmodes.StartArgs if onWin else launchmodes.PortableLauncher

        if port == 80 and not web80_started:
            web80_started = True
            spawner('server80', 
                    'Internet/Web/webserver.py Internet/Web')()

        elif port == 8000 and not web8000_started:
            web8000_started = True
            spawner('server8000',
                    'Internet/Web/webserver.py Internet/Web/PyMailCgi 8000')()

    site = 'localhost:%s'
    #startLocalWebServers()   # run webserver on port 80 and 8000 on localhost
    #print('servers started') # now delayed until demo selected in GUI

    class WebLauncher(Launcher):      # customize to start server first
        def run(self, cmdline):
            port, cmdline = cmdline.split('@')
            startLocalWebServers(int(port))
            Launcher.run(self, cmdline)

    demoButton('PyMailCGI',
               'Browser-based pop/smtp email interface',
               '8000@LaunchBrowser.pyw -live pymailcgi.html '+ (site % 8000),
               ['%s/webserver.py' % pagepath] + pymailcgifiles,
               launcher=WebLauncher)

    demoButton('PyInternet',
               'Main Internet demos launcher page',
               '80@LaunchBrowser.pyw -live PyInternetDemos.html ' + (site % 80),
               ['%s/webserver.py' % pagepath,
                '%s/PyInternetDemos.html' % pagepath],
                launcher=WebLauncher)

    # PyErrata removed in 3rd Ed

################################################################################
# toggle info message box font once a second
################################################################################

def refreshMe(info, ncall):
    slant = ['normal', 'italic', 'bold', 'bold italic'][ncall % 4]
    info.config(font=('courier', 20, slant))
    Root.after(1000, (lambda: refreshMe(info, ncall+1)) )

# To try: bind mouse entry events to change info text when over a button

################################################################################
# unhide/hide status box on info clicks
################################################################################

Stat.iconify()
def onInfo():
    if Stat.state() == 'iconic':
        Stat.deiconify()
    else:
        Stat.iconify()  # was 'normal'

################################################################################
# pop up a few web link buttons if connected
################################################################################

radiovar = StringVar() # use a global

def onLinks():
    popup = PopupWindow('PP4E web site links')
    links = [("Book",
                   'LaunchBrowser.pyw -live about-pp.html www.rmi.net/~lutz'),
             ("Python",
                   'LaunchBrowser.pyw -live index.html www.python.org'),
             ("O'Reilly",
                   'LaunchBrowser.pyw -live index.html www.oreilly.com'),
             ("Author",
                   'LaunchBrowser.pyw -live index.html www.rmi.net/~lutz')]

    for (name, command) in links:
        callback = Launcher((name + "'s web site"), command)
        link = Radiobutton(popup, text=name, command=callback)
        link.config(relief=GROOVE, variable=radiovar, value=name)
        link.pack(side=LEFT, expand=YES, fill=BOTH)
    radiovar.set(name)
    Button(popup, text='Quit', command=popup.destroy).pack(expand=YES,fill=BOTH)

    if InternetMode != '-live':
        from tkinter.messagebox import showwarning
        showwarning('PP4E Demos', 'Web links require an Internet connection')

################################################################################
# finish building main GUI, start event loop
################################################################################

Button(Root, text='Info',  command=onInfo).pack(side=TOP, fill=X)
Button(Root, text='Links', command=onLinks).pack(side=TOP, fill=X)
Button(Root, text='Quit',  command=Root.quit).pack(side=BOTTOM, fill=X)
refreshMe(Info, 0)  # start toggling
Root.mainloop()
