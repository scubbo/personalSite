#!/usr/bin/python
import cgi, os, sys
form = cgi.FieldStorage()

sys.stderr = sys.stdout

sys.stdout.write('Content-Type: text/html\r\n\r\n')

userEmail = form.getvalue('email', 'blank')
userName = form.getvalue('name', 'User')

os.system('echo \'name was ' + userName + ' and email was ' + userEmail + '\' | mutt -s \'Archon Prison output\' scubbojj@gmail.com')

sys.stdout.write('name was ' + userName + ' and email was ' + userEmail)
