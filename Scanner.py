import RealClearPolitics
from fnmatch import fnmatch

def is_gov(l):
    """returns true if a URL refers to a gov race"""
    pattern = 'http://www.realclearpolitics.com/epolls/????/governor/??/*-*.html'
    return fnmatch(l, pattern)

def find_governor_races(html):
    dom = web.Element(html)
    links = [a.attributes.get('href', '') for a in dom.by_tag('a')] 
    links = [l for l in links if is_gov(l)]
    #eliminate duplicates!
    links = list(set(links))
    return links

def race_results(url):
    dom=web.Element(requests.get(url).text)
    
    table=dom.by_tag('div#polling-data-rcp')[0]
    result_data=table.by_tag('tr.final')
    td=result_data.by_tag('td')
    
    results= [float(t.content) for t in td[3:-1]]
    tot = sum(results)/100
    
    #get table headers
    headers = table.by_tag('th')
    