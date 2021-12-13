#!/usr/bin/env python
# coding: utf-8

# In[7]:


# import libraries
import pandas as pd


# loading dataset
df = pd.read_csv('resources/FlightSalesClean.csv')
print('loading Dataset Compelete!')


# In[10]:


# to calculate average of money spent for ticket by every user
dataset = df.groupby(['user_id'])['price'].mean()

print('each user’s average table is:')
print(dataset)


# In[11]:


#export the dataset with csv format
export_csv = dataset.to_csv(r'Question1.csv')

print('Done Exporting user’s average table ')


# In[12]:


# calculating number of users using user_id
number_of_users = dataset.count()

# price column's sum
price_sum = df['price'].sum()

# calculating sum of prices per number of users
price_per_user = price_sum / number_of_users
print('Overall average =', round(price_per_user , 2))


# In[ ]:




