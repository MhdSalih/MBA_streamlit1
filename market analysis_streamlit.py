#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import streamlit as st


# In[11]:


st.write("""
# MARKET BASKET ANALYSIS """)


# In[14]:


df=pd.read_csv("new_MBA.csv")
df = df.drop(df.columns[0], axis=1)
df


# In[15]:


st.write(df)


# In[ ]:




