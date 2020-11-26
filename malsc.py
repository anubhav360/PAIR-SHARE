# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:15:17 2020

@author: Anubhav Sharma
"""
import requests
def mals(file_dest):      
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    
    params = {'apikey': 'cd3fcf8cb9b77299a98f29bc1aa4db1e22fe105032da21a88910643ec309cb53'}
    
    files = {'file': (file_dest, open(file_dest, 'rb'))}
    
    response = requests.post(url, files=files, params=params)
    
    #print(response.json())
    res=response.json()['resource']
    #print (res)
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    
    params = {'apikey': 'cd3fcf8cb9b77299a98f29bc1aa4db1e22fe105032da21a88910643ec309cb53', 'resource': res}
    
    response = requests.get(url, params=params)
    if ('positives' in response.json()):
        print (response.json()['positives'])
        if(int(response.json()['positives'])>0):
            return 1
        else:
            return 0
    else:
        return 2