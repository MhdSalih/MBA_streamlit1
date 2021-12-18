

# In[10]:


import streamlit as st
import pandas as pd
import numpy as np




# In[15]:


st.title('MARKET BASKET ANALYSIS')
st.write('')

    
df=pd.read_csv("new_MBA.csv")
df = df.drop(df.columns[0], axis=1)



st.write(df)
