import cgi 
import urllib2 
import json

def getTorrents(query):
        torrentList = []
        torrentList += getTorrentsFromIsoHunt(query)
        torrentList = filterForRepeats(torrentList)
        return torrentList

def getTorrentsFromIsoHunt(query):
        queryString = urllib2.quote(query)
        url = 'http://isohunt.com/js/json.php?ihq=' + queryString + '&sort=seeds'
        jsonResponse = urllib2.urlopen(url).read()
        items = json.loads(jsonResponse)['items']['list']
        returnValue = []
        for item in items:
                returnValue.append({'title':item['title'], 'url':item['enclosure_url'], 'size':item['size'], 'seeds':item['Seeds'], 'hash':item['hash']})
        return returnValue

def filterForRepeats(torrentList):
        with file('/mnt/hd1/data/torrents/hashes', 'r') as f:
                hashes = f.read().split('\n')
        return filter(lambda x: x['hash'] not in hashes, torrentList)
