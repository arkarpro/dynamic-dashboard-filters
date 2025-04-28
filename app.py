import pandas as pd
import streamlit as st

df = pd.read_csv("populationdata.csv")

st.markdown("## Step-by-Step Dynamic-Dashboard-Filters")
st.dataframe(df)
