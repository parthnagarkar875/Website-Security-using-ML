# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:19:16 2019

@author: Parth
"""
from urllib.parse import urlparse

def get_domain_name(url):
    try:
        url=get_subdomain_name(url).split('.')
        return url[-2]+'.'+url[-1]
    except:
        return '' 

def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""
    
    
