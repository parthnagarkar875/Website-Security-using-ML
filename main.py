# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:42:18 2019

@author: Parth
"""
from queue import Queue
from general import *
from domain import *
from spider import Spider
import threading

'''
The variables declared in capital letters are meant to kept constant and indicate that
any other programmer who is viewing the code shouldn't change the value of these
variables.
'''
#PROJECT_NAME='test'
HOMEPAGE=input("Enter the URL of the website: ")
DOMAIN_NAME=get_domain_name(HOMEPAGE)
sp=DOMAIN_NAME.split('.')
PROJECT_NAME=sp[0]
QUEUE_FILE=PROJECT_NAME+"/queue.txt"
CRAWLED_FILE=PROJECT_NAME+"/crawled.txt"
DEFECT_FILE=PROJECT_NAME+"/defect.txt"
NUMBER_OF_THREADS=8
queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)
      
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)     #target specifies the function the threads will work/execute on. 
        t.daemon=True     #Daemon threads are killed automatically when the program stops. Otherwise we will have to kill all separately. 
        t.start()
        
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()       #Indicates that the current enqueued task is complete. 

def create_jobs():
    for i in file_to_set(QUEUE_FILE):
        queue.put(i)
    queue.join()                #Blocks the queue until all the elements have been pulled and processed. 
    crawl()

def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(len(queued_links),' links in the queue.')
        create_jobs()
        


create_workers()
crawl()

