#!/usr/bin/python
import json
import torrents

print "Content-type: application/json"
print

form=cgi.FieldStorage()
query = form.getvalue("query")

op = torrents.getTorrents(query)
print json.dumps(op)
