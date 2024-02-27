import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict function
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    predicted_species = class_names[prediction[0]]
    return predicted_species

# Streamlit app
def main():
    st.title('Iris Flower Species Prediction')
    st.write('This app predicts the species of Iris flowers based on their sepal and petal dimensions.')

    # Input fields
    sepal_length = st.slider('Sepal Length', min_value=0.1, max_value=7.9, step=0.1)
    sepal_width = st.slider('Sepal Width', min_value=0.1, max_value=4.4, step=0.1)
    petal_length = st.slider('Petal Length', min_value=0.1, max_value=6.9, step=0.1)
    petal_width = st.slider('Petal Width', min_value=0.1, max_value=2.5, step=0.1)

    if st.button('Predict'):
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)
        st.write(f'Predicted Species: {prediction}')

if __name__ == "__main__":
    main()
