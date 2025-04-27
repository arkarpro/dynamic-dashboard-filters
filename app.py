import pandas as pd   #inport pandas
import streamlit as st #import streamlist to show fig target to enduser
df_org = pd.read_csv("populationdata.csv") #read csv by using pandas

st.markdown("## Step-by-Step Dynamic-Dashboard-Filters") #added a title
st.info("***please check below table with scorlable for the original data at below table, you can download it***") #add an info
st.dataframe(df_org, height= 200, width=800) #put data frame size h200, w800

df = df_org.copy() # Always work on a copy


