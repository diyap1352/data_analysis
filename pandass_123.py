#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


sd = pd.DataFrame ({
    "Name" : ["Deeya","Vaishali","Dhruv","Rahul","Naeem"],
    "Age" : [18,23,20,21,19]
})
sd


# In[6]:


sd.loc[3]


# In[7]:


dm = pd.DataFrame ({
    "Name" : ["Deeya",np.nan,"Dhruv","Rahul","Naeem"],
    "Age" : [18,23,np.nan,21,19]
})
dm


# In[8]:


p = dm.dropna()
p


# In[9]:


import random


# In[10]:


lst = ("rahul","deeya","vaishali","dhruv","naeem")
print(random.sample(lst , k=1))


# In[11]:


sd.sample(n=2)


# In[12]:


sd["Age"].where(sd["Age"] < 20)


# In[14]:


sd["Age"].where(sd["Age"] < 20, 0)


# In[19]:


names = ["Vaishali","Deeya"] 
sd[sd.Name.isin(names)]


# In[18]:


sd.replace("Deeya","dd")


# In[20]:


sd.nsmallest(2,"Age")


# In[21]:


sd.nlargest(2,"Age")


# In[22]:


sd.groupby("Name")["Age"].sum()


# In[23]:


dm["Age"].fillna(dm["Age"].mean(),inplace = True)


# In[24]:


dm


# In[25]:


dm["Name"].fillna(dm["Name"].mode(),inplace = True)
dm


# In[26]:


sd.rename(columns = {"Name" : "N_Name","Age" : "A_Age"})


# In[ ]:




