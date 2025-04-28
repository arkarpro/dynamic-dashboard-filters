import pandas as pd   # Import pandas for data manipulation
import streamlit as st # Import streamlit to display the dashboard
df_org = pd.read_csv("populationdata.csv") # Read CSV using pandas

st.markdown("#### Step-by-Step Guide: Building Dynamic Dashboard Filters") # Title
st.info("***Explore the original dataset below. You can scroll through the table and download it if needed.***") # Info message
st.dataframe(df_org, height=200, width=800) # Display dataframe with specific height and width

df = df_org.copy() # Always work on a copy of the original dataframe
df['Male'] = df['Male'].str.replace(',', '', regex=True).str.strip()  # Remove commas and spaces
df['Male'] = pd.to_numeric(df['Male'], errors='coerce') # Convert Male column to numeric
df['Female'] = df['Female'].str.replace(',', '', regex=True).str.strip() # Remove commas and spaces
df['Female'] = pd.to_numeric(df['Female'], errors='coerce') # Convert Female column to numeric

# State/Region filter
rg_list = ['All'] + sorted(df['State_Region'].dropna().unique().tolist()) # List of regions
selected_rg = st.selectbox("Choose State/Region", rg_list) # Dropdown for region selection

if selected_rg != 'All': # Apply filter if region is selected
    df = df[df['State_Region'] == selected_rg]

# District filter
dt_list = ['All'] + sorted(df['District'].dropna().unique().tolist()) # List of districts
selected_dt = st.selectbox("Choose District", dt_list) # Dropdown for district selection

if selected_dt != 'All': # Apply filter if district is selected
    df = df[df['District'] == selected_dt]

# Township filter
tsp_list = ['All'] + sorted(df['Township'].dropna().unique().tolist()) # List of townships
selected_tsp = st.selectbox("Choose Township", tsp_list) # Dropdown for township selection

if selected_tsp != 'All': # Apply filter if township is selected
    df = df[df['Township'] == selected_tsp]

st.info("***You can now check and download your selected data.***")
st.dataframe(df)

# Bonus tips
male = df['Male'].sum() # Sum of male population
female = df['Female'].sum() # Sum of female population

# Create two columns for the metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Male Population", f"{male:,}")

with col2:
    st.metric("Total Female Population", f"{female:,}")

# Future Plans Section
st.markdown("""
နောက်ထပ် လုပ်ဆောင်သွားမယ့်အကြောင်းကတော့ —

[Titanic Dashboard](https://titanic-eda-dashboard-dkd68fsawayaumwjkkow85.streamlit.app/)

နဲ့ [Target vs Actual Dashboard](https://targetvsactual-arkarpro.streamlit.app/)  နှစ်ခုကို ပြန်လည်သုံးသပ်ပြီး 
Data Structure နဲ့ Design တွေကို အသုံးချကာ ပိုမိုပြည့်စုံတဲ့ Dynamic Dashboard တစ်ခုကို အစကနေ တည်ဆောက်သွားဖို့ စီစဉ်ထားပါတယ်။

ထို့အပြင် Social Media Data ကို အခြေခံပြီး Dependent Filters နည်းနဲ့ Dashboard တစ်ခုလည်း တည်ဆောက်ဖို့ စတင်ထားပါတယ်။
Source Code နဲ့ Demo App တွေလည်း မကြာခင် GitHub နဲ့ Streamlit Cloud မှာ မျှဝေပေးသွားမှာပါ။
            Data Dashboard လေ့လာနေသူ မိတ်ဆွေတွေအနေနဲ့ လည်း တူတူလုပ်ကြမလား ဆိုတာ စိတ်ဝင်စားနေပါတယ်။
ချိတ်ဆက်ချင်ရင်၊ တူတူတည်ဆောက်ချင်ရင် LinkedIn / Contact မှာလည်း ဆက်သွယ်နိုင်ပါတယ်နော်။

Info to visit
             
➡️ [GitHub - Arkar](https://github.com/arkarpro)  
➡️ [LinkedIn - Arkar](https://www.linkedin.com/in/arkar-linn-datapro)
""")