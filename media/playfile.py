import os, sys, mimetypes, webbrowser
helpmsg = """
Sorry: can't find a media player for '%s' on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""
def trace(*args): print(*args) # with spaces between
##################################################################################
# player techniques: generic and otherwise: extend me
##################################################################################
class MediaTool:
    def __init__(self, runtext=''):
        self.runtext = runtext
    def run(self, mediafile, **options): # most ignore options
        fullpath = os.path.abspath(mediafile) # cwd may be anything
        self.open(fullpath, **options)
class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w') # spawn shell tool
        player.write(media.read()) # send to its stdin
class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile # run any cmd line
        os.system(cmdline) # use %s for filename
class Winstart(MediaTool): # use Windows registry
    def open(self, mediafile, wait=False, **other): # or os.system('start file')
        if not wait: # allow wait for curr media
            os.startfile(mediafile)
        else:
            os.system('start /WAIT ' + mediafile)
class Webbrowser(MediaTool):
    # file:// requires abs path
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)

audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'), # os.popen().write()
    'linux2': Cmdline('cat %s > /dev/audio'), # on zaurus, at least
    'sunos4': Filter('/usr/demo/SOUND/play'), # yes, this is that old!
    'win32': Winstart() # startfile or system 
    #'win32': Cmdline('start %s')
}

videotools = {
    'linux2': Cmdline('tkcVideo_c700 %s'), # zaurus pda
    'win32': Winstart(), # avoid DOS pop up
}
imagetools = {
    'linux2': Cmdline('zimager %s'), # zaurus pda
    'win32': Winstart(),
}
texttools = {
    'linux2': Cmdline('vi %s'), # zaurus pda
    'win32': Cmdline('notepad %s') # or try PyEdit?
}
apptools = {
    'win32': Winstart() # doc, xls, etc: use at your own risk!
}

mimetable = {
    'audio': audiotools,
    'video': videotools,
    'image': imagetools,
    'text': texttools, # not html text: browser
    'application': apptools
}

def trywebbrowser(filename, helpmsg=helpmsg, **options):
    trace('trying browser', filename)
    try:
        player = Webbrowser() # open in local browser
        player.run(filename, **options)
    except:
        print(helpmsg % filename) # else nothing worked

def playknownfile(filename, playertable={}, **options):
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options) # specific tool
    else:
        trywebbrowser(filename, **options) # general scheme

def playfile(filename, mimetable=mimetable, **options):
    contenttype, encoding = mimetypes.guess_type(filename) # check name
    if contenttype == None or encoding is not None: # can't guess
        contenttype = '?/?' # poss .txt.gz
    maintype, subtype = contenttype.split('/', 1) # 'image/jpeg'
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options) # special case
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options) # try table
    else:
        trywebbrowser(filename, **options) # other types

if __name__ == '__main__':
    # media type known
   # playknownfile('sousa.au', audiotools, wait=True)
   # playknownfile('ora-pp3e.gif', imagetools, wait=True)
   # playknownfile('ora-lp4e.jpg', imagetools)
    # media type guessed
    input('Stop players and press Enter')
    playfile('D:\\Tmp\\avt.jpg') # image/jpeg
    playfile('D:\\Craft\\3d-js\\arcgis\\1\\1.html') # text/html
    playfile('D:\\Craft\\aspnetcore\\AspCoreSamples\\run.txt') # text/plain
    playfile('D:\\TeamViewer13.1.3629.rar') # app
    playfile('D:\\ccwc.xls') # app
    playfile('D:\\Craft\\VideoLab\\ffmpeg-lab\\ffmpeg-3.4.1-win64-static\\bin\\chop-video-to-img\\video\\output.mp4', wait=True) # audio/basic
    input('Done') # stay open if clicked
