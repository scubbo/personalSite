#!/usr/bin/python
import cgi
import os
import sys
import json

form = cgi.FieldStorage()

sys.stderr = sys.stdout

sys.stdout.write('Content-Type: application/json\r\n\r\n')

mylist = ['hello', 'world']
jsonOutput = json.dumps(mylist)

sys.stdout.write(jsonOutput)
