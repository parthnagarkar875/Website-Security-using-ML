"""
Created on Thu Sep 26 20:47:25 2019

@author: Parth
"""
'''
HTMLParser class isn't designed to be used out of the box. So we have to inherit it
and override its methods.
'''

from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
    
    def handle_starttag(self,tag,attrs):
    #In this method, we will find all the anchor tags and the links they are directing to.
        if tag=='a':
            for(attribute,value) in attrs:
                if attribute=='href':
                    url=parse.urljoin(self.base_url,value) #joining the base_url to the relative URL.
                    self.links.add(url)
                    
    def error(self,message):
        pass

    def page_links(self):
        return self.links
    
