#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)


# In[3]:


soup=BeautifulSoup(page.text,'html')
table=soup.find_all('table')[1]
title_list=[title.text.strip() for title in table.find_all('th')]


# In[5]:


df = pd.DataFrame(columns=title_list)


# In[6]:


rows_list= table.find_all('tr')
for i in rows_list[1: ]:
    #print(table.find_all('td'))
    data_list=[data.text.strip() for data in i.find_all('td')]
    #print(data_list)
    lenght=len(df)
    df.loc[lenght]=data_list


# In[8]:


df.to_csv(r'C:\Users\Asus\companies_list')

