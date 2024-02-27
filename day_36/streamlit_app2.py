import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Random Forest Classifier App
## Made by Danish AZeem
This app predicts the type of iris based on sepal length, sepal width, petal length, and petal width.""")

st.sidebar.header('Change IRIS parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4) 
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('IRIS parameters') 
st.write(df)

iris = sns.load_dataset('iris')

st.subheader('Iris Dataset') 
st.write(iris.head(10))

st.subheader("Plotly Box Plots")
fig = px.box(iris, x="species", y="petal_length", color="species")
st.plotly_chart(fig)

st.subheader("Gapminder GDP Plot, Animated")
df1 = px.data.gapminder()
fig2 = px.scatter(df1, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                 size="pop", color="continent", hover_name="country", log_x=True, size_max=55,
                 range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig2)

fig3 = px.bar(df1, x="continent", y="pop", color="continent", animation_frame="year", animation_group="country", 
              range_y=[0,4000000000])
st.plotly_chart(fig3)

fig4 = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_length', color='species')
st.plotly_chart(fig4)

x = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris['species']

model = RandomForestClassifier() 
model.fit(x, y)

prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris['species'].unique())

st.subheader('Prediction')
st.write(prediction[0])

st.subheader('Prediction Probability')
st.write(prediction_proba)
