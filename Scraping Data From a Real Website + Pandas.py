#!/usr/bin/env python
# coding: utf-8

# # Scraping Data From a Real Website + Pandas

# In[3]:


# import beautifulsoup library from bs4


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


# assign the web-link to url
# request url via requests.get and assign to page
# using the beautifulsoup library extract page in text form


# In[6]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup =  BeautifulSoup(page.text, 'html')


# In[9]:


print(soup)


# In[23]:


# find all in 'table' and index it to position 1


# In[22]:


soup.find_all('table')[1]


# In[45]:


# assign it the above line to 'table'


# In[24]:


table = soup.find_all('table')[1]


# In[25]:


print(table)


# In[29]:


# filter the noise and request for only the title head ('th') in table and assign it to world_titles


# In[41]:


world_titles = table.find_all('th')


# In[42]:


print(world_titles)


# In[43]:


# looping through 'world title' to  get the title in text format


# In[46]:


world_table_titles =[title.text.strip() for title in world_titles]


# In[47]:


print(world_table_titles)


# In[48]:


# import panda library


# In[49]:


import pandas as pd


# In[51]:


# turns into a dataframe


# In[79]:


df = pd.DataFrame(columns = world_table_titles)


# In[80]:


df


# In[96]:


column_data = table.find_all('tr')


# In[100]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]


# In[101]:


length = len(df)
df.loc[length] = individual_row_data


# In[102]:


df


# In[104]:


df.to_csv(r'C:\Users\DELL\Documents\Python Tutorial\companies.csv')


# In[ ]:




