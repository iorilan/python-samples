
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'   # where your HTML files and cgi-bin script directory live
port   = 6010    # http://servername/ if 80, else use http://servername:xxxx/

if len(sys.argv) > 1: webdir = sys.argv[1]             # command-line args
if len(sys.argv) > 2: port   = int(sys.argv[2])        # else default ., 80
print('webdir "%s", port %s' % (webdir, port))

os.chdir(webdir)                                       # run in HTML root dir
srvraddr = ('', port)                                  # my hostname, portnumber
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()                                # serve clients till exit
