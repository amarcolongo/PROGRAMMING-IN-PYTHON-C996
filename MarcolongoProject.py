#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import csv
import numpy as np
from bs4 import BeautifulSoup


# In[2]:


url = 'https://www.census.gov/programs-surveys/popest.html'    # This is the url provided in the project description


# In[3]:


r = requests.get(url)


# In[4]:


raw_html = r.text


# In[5]:


print(raw_html); # This will print out the html code of the website at the time I did the scrapping


# In[6]:


soup = BeautifulSoup(raw_html, 'html.parser')


# In[7]:


links = soup.find_all("a")


# In[8]:


print('Number of links retrieved: ', len(links))


# In[9]:


MySet = set()


# In[10]:


for link in links:
    hrefs = str(link.get("href"))
    if hrefs.startswith('None'):
            ''
    elif hrefs.startswith('#http'):
            MySet.add(hrefs[1:])
    elif hrefs.startswith('#'):
            ''
    elif hrefs.startswith('/'):
            MySet.add ('https://www.census.gov' + hrefs)
    elif hrefs.endswith('.gov'):
            MySet.add (hrefs + '/')
    else:
            MySet.add(hrefs)


# In[11]:


f = open("MarcolongoFinalAssignment.csv", "w") 
writer = csv.writer(f, delimiter= ' ', lineterminator = '\r')


# In[12]:


MyList = []
ctr = 0
for x in MySet:
        MyList.append(x)
        if not MyList:
                ''
        else:
                writer.writerow(MyList)
                del MyList[:]
                ctr += 1


# In[13]:


print('Number of URLs written to CSV', ctr)


# In[14]:


f.close()

