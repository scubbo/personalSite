#!/usr/bin/python
import os

print 'Content-type: application/json'
print

outputString = '['

cacheFiles = os.listdir('../tweetCache/')
cacheFiles.sort(reverse=True)
for i in cacheFiles:
    with file('../tweetCache/'+i,'r') as f:
        outputString += f.read() + ','

print outputString[:-1] + ']'
