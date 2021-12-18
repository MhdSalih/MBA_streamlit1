#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st


# In[3]:


st.write("""
# MARKET BASKET ANALYSIS """)


# In[8]:


df=pd.read_csv("my_MBA.csv")
df = df.drop(df.columns[[0, 1]], axis=1)
df


# In[9]:


st.write(df)


# In[ ]:




