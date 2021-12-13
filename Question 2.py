#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from IPython.display import display

D = pd.read_csv('resources/FlightSalesClean.csv')
print('loading Dataset Complete!')


# In[2]:


sum_price_user = D.groupby('user_id')['price'].sum()   #how much each user has paid in total
sum_price_user  = sum_price_user.sort_values(ascending=False)  #sort users based on their paid money 
sum_price_user = sum_price_user.to_frame().reset_index() 

# this list will become the score column later, we append scores to this
score_list=[]

#let's calculate each user's score
for i in sum_price_user['price']:
    i = int(i)
    if i > 900:
        #for users with total expenditure more than 900, every 100 more expenditure adds 5 score to them.
        #so if you spend 999 you get nothing if you spend 1000 you get 5 scores, 1050 means 5 score, 1100 10 score and so on
        score_list.append((((i-900)//100)*5))
    else:
        score_list.append(0)

#add a column named score and fill it with score list
sum_price_user['score']=score_list


# In[3]:


#give the final sum_price_user DF a better look:

sum_price_user.rename(columns={'price':'total expenditure (*10^3 T)'}, inplace=True)

sum_price_user = sum_price_user.round(3)


# In[4]:


print('top 10 customers and their score and their total expenditures are:')
display(sum_price_user.head(10))

