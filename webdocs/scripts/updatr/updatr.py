#!/usr/bin/python
import cgi
import os
import sys
import json

def readUpdate(updatable):
	response = {}

	# Only allow the script to read from pre-defined files
	with file('updatables', 'r') as updatablesFile:
		updatables = updatablesFile.read().split('\n')

	if updatable not in updatables and not updatable.startswith('/tmp/updatables/'):
		response['status'] = 'ERROR'
		response['message'] = 'Only predetermined files can be read by updatr'
		return response

	with file(updatable, 'r+') as uf:
		# Read, split into lines, and filter out empty strings
		readData = filter(lambda x: x, uf.read().split('\n'))
		# Empty file
		uf.seek(0)
		uf.truncate()

	if readData:
		response['status'] = 'SUCCESS'
		response['data'] = readData
	else:
		response['status'] = 'END'

if __name__ == '__main__':
	sys.stdout.write('Content-Type: application/json\r\n\r\n')

	form = cgi.FieldStorage()
	updatable = form.getvalue('updatable')

        response = readUpdate(updatable)
        jsonResponse = json.dumps(response)
        sys.stdout.write(jsonResponse)
