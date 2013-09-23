#!/usr/bin/python
import cgi
import json

print "Content-type: application/json"
print

form = cgi.FieldStorage()
query = form.getvalue('query')

queryList = json.loads(query)

torrentList = 
