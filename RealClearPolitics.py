import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import re
from pattern import web


def get_poll_xml(poll_id):
    url= "http://charts.realclearpolitics.com/charts/"+str(poll_id)+".xml"
    r=requests.get(url)
    dom=web.Element(r.text)
    for val in dom.by_tag('series'):
        #v= val.by_tag("value")[15].content
        g = [g.content for g in val.by_tag('value')]
    print g
    return dom

get_poll_xml(1044)

def _strip(s):
    """This function removes non-letter characters from a word
    for example _strip('Hi there!') == 'Hi there'
    """
    return re.sub(r'[\W_]+','',s)

def plot_colors(xml):
    dom = web.Element(xml)
    result={}
    for graph in dom.by_tag('graph'):
        title = _strip(graph.attributes['title'])
        result[title]= graph.attributes['color']
    return result

def rcp_poll_data(xml):
    
    
    
    
    touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/alvinlee123/Webscraping.git
git push -u origin master