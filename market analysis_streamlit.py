#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import pandas as pd
import numpy as np




# In[15]:


st.title('MARKET BASKET ANALYSIS')
st.write('')

upload_file=st.sidebar.file_uploader(label="upload your csv or excel file",type=["csv","xlsx"])

global df
if upload_file is not None:
  print(upload_file)
  print('hello')
  try:
    df = pd.read_csv(upload_file)
  except Exception as e:
    print(e)
    df = pd.read_excel(uploade_file)
    


# In[16]:


st.write(df)
