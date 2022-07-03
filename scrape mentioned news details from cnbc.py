#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page = requests.get('https://www.cnbc.com/world/?region=world%20:')


# In[5]:


page


# In[6]:


soup = BeautifulSoup(page.content)
soup


# In[9]:


titles = []

for i in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
     titles.append(i.text)
        
titles


# In[13]:


time = []
for i in soup.find_all('span',class_="LatestNews-wrapper"):
    time.append(i.text)
    
time


# In[15]:


link = []
for i in soup.find_all('span',class_="RiverByline-authorByline"):
    link.append(i.text)
    
link


# In[21]:


print(len(titles),len(time),len(link))


# In[24]:


import pandas as pd
df = pd.DataFrame({'Titles':titles})
df


# In[28]:


print(len(time))


# In[33]:


import pandas as pd
df = pd.DataFrame({'Time':time})
df


# In[30]:


print(len(link))


# In[35]:


import pandas as pd
df = pd.DataFrame({'Link':link})
df


# In[ ]:




