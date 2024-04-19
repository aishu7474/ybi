#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('movies.csv')
ratings=pd.read_csv('ratings.csv')
df


# In[3]:


df.head()


# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import scipy.sparse as sp
from scipy.sparse.linalg import svds


# In[9]:


ratings


# In[10]:


ratings.head()


# In[13]:


ratings.shape


# In[14]:


ratings.info()


# In[16]:


ratings.describe()


# In[17]:


ratings.hist(column='userId')


# In[ ]:




