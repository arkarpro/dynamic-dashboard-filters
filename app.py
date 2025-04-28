import pandas as pd   #inport pandas
import streamlit as st #import streamlist to show fig target to enduser
df_org = pd.read_csv("populationdata.csv") #read csv by using pandas

st.markdown("#### Step-by-Step Guide: Building Dynamic Dashboard Filters") #added a title
st.info("***Please explore the original dataset below. You can scroll through the table, and download it if needed.***") #add an info
st.dataframe(df_org, height= 200, width=800) #put data frame size h200, w800

df = df_org.copy() # Always work on a copy
df['Male'] = df['Male'].str.replace(',', '', regex=True).str.strip()  # remove commas and spaces
df['Male'] = pd.to_numeric(df['Male'], errors='coerce')
df['Female'] = df['Female'].str.replace(',','', regex=True).str.strip()
df['Female'] = pd.to_numeric(df['Female'],errors='coerce')

#state/region filter---------------------------------------------------------------------------------
rg_list = ['All'] + sorted(df['State_Region'].dropna().unique().tolist()) # set a rg list All + data from csv .. drop/unique/tolist
selected_rg = st.selectbox("Choose State/Region", rg_list) #set a rg select box placeholder

if selected_rg != 'All': # add a condition if user not select 'All'
    df = df[df['State_Region'] == selected_rg] # df will be filtered in 'state_region' coloumn by selected_rg as choose

#district filter  ------------------------------------------------------------------------------------
dt_list = ['All'] + sorted(df['District'].dropna().unique().tolist())
selected_dt = st.selectbox("Choose District", dt_list)

if selected_dt != 'All': # add a condition if user not select 'All'
    df = df[df['District'] == selected_dt] # df will be filtered in 'District' coloumn by selected_dt as above choose

#township filter --------------------------------------------------------------------------------------
tsp_list = ['All'] + sorted(df['Township'].dropna().unique().tolist())
selected_tsp = st.selectbox("Choose Township", tsp_list)

if selected_tsp != 'All': # add a condition if user not select 'All'
    df = df[df['Township'] == selected_tsp] # df will be filtered in 'township' coloumn by selected_dt as above choose

st.info ("***Now you can check and download that your selected data***")
st.dataframe(df)

st.markdown(" Bonus tips")

# Bonus tips
male = df['Male'].sum()
female = df['Female'].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Male Population", f"{male:,}")

with col2:
    st.metric("Total Female Population", f"{female:,}")




