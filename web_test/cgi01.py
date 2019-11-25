#
#
import cgi 
form = cgi.FieldStorage()
print('Content-type: tetx/html\n')
print('<title>Reply page</title>')
if not 'user' in form:
    print('<h1> who are you?</h1>')
else:
    print('<h1> hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))

