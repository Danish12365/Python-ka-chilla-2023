import streamlit as st
import seaborn as sns

st.header("This is header")

st.text("This is a text")

st.header("This is over time")

df = sns.load_dataset("iris")
st.write(df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].head())

st.bar_chart(df["sepal_length"])
st.line_chart(df["sepal_length"])







