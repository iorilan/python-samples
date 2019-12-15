import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable # use sys in newer pys

def fixWindowsPath(cmdline):
    splitline = cmdline.lstrip().split(' ') # split on spaces
    fixedpath = os.path.normpath(splitline[0]) # fix forward slashes
    return ' '.join([fixedpath] + splitline[1:]) # put it back together
class LaunchMode:
    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self): # on call, ex: button press callback
        self.announce(self.what)
        self.run(self.where) # subclasses must define run()
    def announce(self, text): # subclasses may redefine announce()
        print(text) # methods instead of if/elif logic
    def run(self, cmdline):
        assert False, 'run must be defined'
class System(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pypath, cmdline))
class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath + ' ' + cmdline) # assume nothing to be read
class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split() # convert string to list
        if os.fork() == 0: # start new child process
            os.execvp(pypath, [pyfile] + cmdline) # run new program in child
class Start(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        cmdline = fixWindowsPath(cmdline)
        os.startfile(cmdline)
class StartArgs(LaunchMode):
    def run(self, cmdline):
        assert sys.platform[:3] == 'win'
        os.system('start ' + cmdline) # may create pop-up window
class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))
class Top_level(LaunchMode):
    def run(self, cmdline):
        assert False, 'Sorry - mode not yet implemented'

if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass

def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher() # no block

    input('system mode...')
    System(file, file)() # blocks

    if sys.platform[:3] == 'win':
        input('DOS start mode...') # no block
        StartArgs(file, file)()
if __name__ == '__main__': selftest()