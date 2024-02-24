# import libraries
import seaborn as sns
import plotly.express as px
import pandas as pd
import streamlit as st

# st.title("Plotly and Streamlit ko mila k app bnana")
# df = px.data.World_Indicators()
# st.write(df)

st.title("Plotly and Streamlit ko mila k app bnana")
df = pd.read_csv(r'C:\Users\Danish\Desktop\Python ka chilla 2023\day_36\world_population.csv')
st.write(df)

st.write(df.columns)

# summmery stat
st.write(df.describe())

# data management
years_option = df["Country"].unique()
year = st.selectbox('Which year should we plot?', years_option, 0)
df =  df[df["Country"] == year]

# plotting with Plotly Express
fig = px.scatter(df, x="2020 Population", y="Rank", size="Population", color="continent", hover_name="country", log_x=True, size_max=60, range_x=[100,100000], range_y=[25,90])

st.write(fig)