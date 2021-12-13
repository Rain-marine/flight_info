#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import libraries

import pandas as pd

# Load dataset
dataset = pd.read_csv('resources/FlightSalesClean.csv')

# bold the result of program to show cutie
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
print(color.BOLD + '## Load dataset compelete ##')


# In[6]:


# to get number of columns and rows:
print('Number of rows is:', dataset.shape[0])
print('Number of columns is:', dataset.shape[1])
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# In[7]:



#get type, total count, and number of nulls for each column, also get total number of columns for each type, range index and total columns
dataset.info(verbose = False)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# In[8]:



#how many unique values each column has? this shows what range of data in each topic we're talking about
print('each coulmn’s unique values are:')
print(dataset.nunique())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# In[9]:



# readable dates using datetime
dataset['departure_date_id'] = pd.to_datetime(dataset['departure_date_id'], format='%Y%m%d')
dataset['request_date_id'] = pd.to_datetime(dataset['request_date_id'], format='%Y%m%d')


# In[11]:



# get the range of each column
print('request_date_id is', dataset['request_date_id'].min(), 'to', dataset['request_date_id'].max())
print('request_time is', dataset['request_time'].min(), 'to', dataset['request_time'].max())
print('departure_date_id is', dataset['departure_date_id'].min(), 'to', dataset['departure_date_id'].max())
print('company is', dataset['company'].min(), 'to', dataset['company'].max())
print('price is', dataset['price'].min(), 'to', dataset['price'].max() , 'and its mean value is:',round(dataset['price'].mean() , 2))
print('month is', dataset['month'].min(), 'to', dataset['month'].max())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# In[ ]:




