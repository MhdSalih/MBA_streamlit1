#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st


# In[12]:


st.write("""
# MARKET BASKET ANALYSIS """)


# In[ ]:


df=pd.read_csv("MBA_data12")
df=pd.DataFrame(df)

# In[11]:


st.dataframe(df)


# In[ ]:




