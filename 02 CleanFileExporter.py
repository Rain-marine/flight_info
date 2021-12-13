#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

D = pd.read_excel('resources/FlightSales.xlsx')

print('Done loading Dataset!')


# In[7]:


#CLEANING DATA FIRST

#delete column "id" because it makes difference between same rows
#D = D.drop(['id'] , axis = 1) #if you want to delete duplicates UNCOMMENT this commnad

# removing the duplicated rows, only keeping one of them
#!!!NOTE: duplicated rows means a user has bought several tickets thus we decide to keep them.
#D = D.drop_duplicates( keep = 'first')

#Drop rows which contain missing values.
D.dropna(inplace = True)

# Get names of indexes for which column user_id has value less than 1
indexNames = D[ D['user_id'] < 1 ].index
# Delete these rows from dataFrame
D.drop(indexNames , inplace=True)

# Get names of indexes for which column departure_date_id has value 0
indexNames2 = D[ D['departure_date_id'] == 0 ].index
# Delete these rows from dataFrame
D.drop(indexNames2 , inplace=True)


# In[8]:


#ADDING THINGS WE NEED TO DATA

# convert column values that we need, to int64 so we can actually work with it later
D['source'] = D['source'].astype('Int64')
D['destination'] = D['destination'].astype('Int64')
#why first to int64 then to str and not directly to str? because it's float,with one zero 
#so if we convert it to srt directly it will be like:15.0 but it should be like:15


# convert date to str so we can seperate month
D['departure_date_id'] = D['departure_date_id'].astype('str')


#seperate  departure month and add a new column named month for Question 6
D['month'] = D.departure_date_id.apply(lambda x: x[4:6])
#the month column is str, we need intigers in case we want to work with its numbers:
D['month'] = pd.to_numeric(D['month'])
D['month'] = D['month'].astype('Int64')


#add a column named path for Question 5
D['path'] = D['source'].map(str)+"-"+D['destination'].map(str)
D['path'] = D['path'].astype('str')




# In[9]:


#everything done! let's reset indexes
D.reset_index(inplace = True , drop = True)


# In[10]:


#export the clean dataframe with csv format to answer questions with
export_csv = D.to_csv(r'resources/FlightSalesClean.csv')

print('Done Exporting CSV File')


# In[ ]:




