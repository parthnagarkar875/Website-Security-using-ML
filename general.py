# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:12:29 2019

@author: Parth
"""

import os
 
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating a new Directory...")
        os.makedirs(directory)
'''
os.makedirs creates a directory in recursive fashion. 
That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
For example consider the following path:

/home/User/Documents/GeeksForGeeks/Authors/ihritik

Suppose we want to create directory ‘ihritik’ but Directory ‘GeeksForGeeks’ and ‘Authors’ are unavailable in the path. 
Then os.makedirs() method will create all unavailable/missing directory in the specified path. ‘GeeksForGeeks’ and ‘Authors’ will be created first then ‘ihritik’ directory will be created. 
'''

def create_file(file_name,url):
    f=open(file_name,'w')
    f.write(url)
    f.close()
    
def create_project_file(project_name,base_url):
    '''
    The queue file will store the URLs to be visited. 
    The crawled file will store the URLs that are visited. To save the cost of revisiting. 
    '''
    queue= project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    if not os.path.isfile(queue):
        create_file(queue,base_url)
    if not os.path.isfile(crawled):
        create_file(crawled,'')
    

def append_to_file(path,url):
    with open(path,'a') as f:
        f.write(url+'\n')

def delete_from_file(path):
    with open(path,'w') as f:
        pass

def file_to_set(file_path):
    links=set()
    with open(file_path,'rt') as f:
        for i in f:
            links.add(i.replace('\n',''))
    return links

def set_to_file(file_path,links):
    delete_from_file(file_path)
    for i in sorted(links):
        append_to_file(file_path,i)
'''
    with open(file_path,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
'''
    



    
    
    