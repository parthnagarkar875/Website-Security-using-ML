# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:23:55 2019

@author: Parth
"""
from urllib.request import urlopen
from linkcrawler import LinkFinder
from general import *
from domain import *
from custom_pred import *

class Spider:
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''    #indicates the path of the queue file
    crawled_file=''  #indicates the path of the crawled file
    queue=set()
    crawled=set()
    #We have used sets to enable faster access to the memory. 
    
    
    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file=Spider.project_name+"/queue.txt"     #file address appending
        Spider.crawled_file=Spider.project_name+"/crawled.txt" 
        self.boot()
        self.crawl_page("First Spider",Spider.base_url)
        
    @staticmethod
    def boot():
        '''
        ->Just as it boots up, it will create a project directory and the files in it.
        
        ->It will also store the contents of the queue and crawled file in the sets so as 
          to perform faster memory access operations.
        '''
        create_project_directory(Spider.project_name)
        create_project_file(Spider.project_name,Spider.base_url)
        Spider.queue=file_to_set(Spider.queue_file)
        Spider.crawled=file_to_set(Spider.crawled_file)
        
    @staticmethod
    def crawl_page(thread_name,page_url):
        if page_url not in Spider.crawled:
            try:
                print(thread_name," now crawling ",page_url)
                print("Queue ", len(Spider.queue), " | Crawled ",len(Spider.crawled))
                Spider.add_links_to_queue(Spider.gather_link(page_url))
                Spider.queue.remove(page_url)
                Spider.crawled.add(page_url)

                Spider.update_files()
                
            except Exception as e:
                print(str(e))
    @staticmethod
    def gather_link(page_url):
        '''
        Algorithm:
            1. Opens the url.
            2. Checks if the webpage opened is an html document. If true, then reads and decodes the document in a string format.
            3. Creates and object of LinkFinder and passes the html_string obtained in step 2 to the LinkFinder class for further processing. 
            4. If there is an error, return an empty set. 
            5. return page links at the end. 
        '''

        html_str=''
        try:        
            response=urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):         #Checks if the document we are crawling is a webpage and then proceeds. 
                a=response.read()
                html_str=a.decode('utf-8')          #Decode into string format for HTMLPraser class. 
            finder=LinkFinder(Spider.base_url,page_url)     
            finder.feed(html_str)       #This will implicitly pass the html_string, call the methods and start the processing. 
        except Exception as e:
            print(str(e))
            return set()        #Returns an empty set. 
        return finder.page_links()      
    
    @staticmethod
    def add_links_to_queue(links):
        '''
        This method checks if the links are not already present in the queue and crawled queue.
        It also checks if the link's domain name is anything other than the domain name we want to crawl on. 
        '''
        for i in links:
            if i in Spider.queue:
                continue
            if i in Spider.crawled:
                continue
            if Spider.domain_name != get_domain_name(i):
                continue
            Spider.queue.add(i)
            
    @staticmethod
    def update_files():
        set_to_file(Spider.queue_file,Spider.queue)
        set_to_file(Spider.crawled_file,Spider.crawled)
        
    
    
    
            
            
    