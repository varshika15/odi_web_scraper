# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:57:24 2019

@author: Varshika Choudhary
"""

import pandas as pd  
from bs4 import BeautifulSoup   
from urllib.request import urlopen as ureq 
import csv

url = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;template=results;type=batting"

page = ureq(url) #opening the URL
soup = BeautifulSoup(page,"html.parser") #parse the html
table = soup.find("tr", { "class" : "data1" })
#print(table.b.text)
tb = soup.find("tbody")

data={}

for x in tb:
    rows = soup.find_all("tr", { "class" : "data1" })
    #print(rows)
for tr in rows:
    cols = soup.find_all("tr", { "class" : "data1" })
    #print(cols)
    for td in cols:
        name = td.td.text.strip()
        runs = td.b.text.strip()
        data[name] = runs
        #print(data)

#dataframe
op = pd.DataFrame({"Player Name (Nationality)": [str(r) for r in data],"Cumilative Runs": [data[r] for r in data]})           
    
#DF to csv
op.to_csv('odi1.csv', sep=',', encoding='utf-8', index = False)    

