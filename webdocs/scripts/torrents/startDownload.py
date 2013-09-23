#!/usr/bin/python

print "Content-Type: text/plain"
print

import cgi
import os
import sys

def cleanTitle(inp):
	return inp.replace(' ', '_').replace('<b>', '').replace('</b>', '')

form = cgi.FieldStorage()
url = form.getvalue('url')
hash = form.getvalue('hash')
title = cleanTitle(form.getvalue('title'))

torrentFilePath = '/mnt/hd1/data/torrents/'

os.system('wget -O ' + torrentFilePath + 'torrent_files/' + title + '.torrent ' + url)
print 'ran wget -O ' + torrentFilePath + 'torrent_files/' + title + '.torrent ' + url

with file(torrentFilePath + 'hashes', 'a') as hashfile:
	hashfile.write(hash + '\n')
