# import libraries 
import pandas as pd 
import plotly.express as px
import streamlit as st

# import dataset
st.title("Plotly and Streamlit ko mila k app bnana")
df = px.data.gapminder()
st.write(df)

st.write(df.columns)

# summmery stat
st.write(df.describe())

# data management
years_option = df["year"].unique()
year = st.selectbox('Which year should we plot?', years_option, 0)
# df =  df[df["year"] == year]

# plotting with Plotly Express
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                  hover_name="country", log_x=True, size_max=60, range_x=[100,100000], range_y=[25,90],
                  animation_frame='year', animation_group='country')

fig.update_layout(width=800, height=400)
st.write(fig)



