import requests
from BeautifulSoup import BeautifulSoup 
import re
import urllib2
from lxml import html 
url='http://www.twitch.tv/directory/game/Dota%202'

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
soup.prettify()
for a in soup.findAll('div'):
    print a.text