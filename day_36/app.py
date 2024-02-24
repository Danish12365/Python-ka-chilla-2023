import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("kashti ki app")
    st.text("In this app we are going to use the kashti dataset")

    with data_sets:
        st.header("Kashti doob gaye, Hawww!")                                  
        st.text("we will ork with titanic dataset")
        # load dataset
        df = sns.load_dataset("titanic")
        df = df.dropna()  # remove missing values
        st.write(df.head(10))
        st.subheader("kitney admi thay")
        st.bar_chart(df['sex'].value_counts())

        # other plot
        st.subheader("Class kay hesab say firk")
        st.bar_chart(df['sex'].value_counts())
        # subplot
        st.bar_chart(df['age'].sample(10))  # or .head(10)

    with features:
        st.header("These are our app features:")
        st.text("ham as me both sarey future add kiran gay, assaan hi hy")
        st.markdown('1. **Feture 1:** This will tell us pata nahi')
        st.markdown('2. **Feture 2:** This will tell us pata nahi')


with model_training:
    st.header("kashti walon ka kia bna?-model training")
    st.text("we increse dataset increse or decrese")
    # making columns
    input, display = st.columns(2)

with input:
    st.subheader("kashti walon ka kia bna?-model training")


    # phelay column main ap k selection points hun
    max_depth = input.slider("How maney people do you know?", min_value=10, max_value=100, value=20, step=5 )

    # n_estimators
    n_estimators = input.selectbox("How maney people do you know?", options = [100,200,300,400,500,'No Limit'])

# adding list of features
    input.write(df.columns)

    # input features from user
    input_feature = input.text_input("What is your favourite feature?")

    # machine learning model
model =RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

# yahan per aik condition lagay gay
if n_estimators == 'No Limit':
    model = RandomForestRegressor(max_depth=max_depth)
else:
     model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    # define x and y
x = df[[input_feature]]
y = df[['fare']]

    # fit our model
model.fit(x,y)
pred = model.predict(y)
   
        # display metrices 
display.subheader("Mean absolute error of the model is:")
display.write(mean_absolute_error(y,pred))
display.subheader("The squared error of the model is : ")
display.write(mean_squared_error(y,pred))
display.subheader("R2 score of the model is :")
display.write(r2_score(y,pred))

        