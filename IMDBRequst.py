import requests
from pattern import web
import re
from BeautifulSoup import BeautifulSoup 
import pandas 


url='http://www.imdb.com/search/title'
params = dict(sort= 'num_votes,desc',start=1,title_type='feature',year='1950,2012')
r=requests.get(url,params=params)

dom = web.Element(r.text)
print r.url
title=[]
yearZ=[]
for movies in dom.by_tag('td.title'):
    title = movies.by_tag('a')[0].content
    runtime = movies.by_tag("span.runtime")[0].content
    genres = movies.by_tag("span.genre")[0]
    genres = [a.content for a in genres.by_tag('a')]
    print title,runtime, genres
    #title.append(movies.by_tag('a')[0].content)
    
#for year in dom.by_class('year_type'):
 #   yearZ.append(re.sub(r'\W+','',year.content))
    
    
Heh = dict(zip(title,yearZ))
print Heh

