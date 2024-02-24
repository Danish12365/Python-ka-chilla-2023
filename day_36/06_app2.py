# Pehle to saari important libraries import kar lo
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# App ki heading
st.write("""
# Explore different ML models and datasets
Hum dekhtay hain kaun sa best hai in mein se?
""")

# Dataset ka naam ek box mein daal ke sidebar pe laga do
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)

# Classifier ka naam bhi ek dabbe mein daal do
classifier_name = st.sidebar.selectbox(
    'Select classifier',
    ('KNN', 'SVM', 'Random Forest')
)

# Ab humne ek function define karna hai dataset ko load karne ke liye
def get_dataset(dataset_name):
    data = None
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Wine":
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()
    x = data.data
    y = data.target
    return x, y

# Ab is function ko bula lay gayn or X, y variable k equal rakh layn gay
X, y = get_dataset(dataset_name)

# Hum apne data set ki shape ko print kar denge
st.write('Shape of dataset:', X.shape)
st.write('Number of classes:', len(np.unique(y)))

# Next hum different classifier ke parameters ko user input mein add karenge
def add_parameter_ui(classifier_name):
    params = dict() # Create an empty dictionary
    if classifier_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    elif classifier_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    else: # Random forest
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params

# Add parameters UI for the given classifier_name and store them in the params variable
params = add_parameter_ui(classifier_name)

# Define a function to create a classifier based on classifier_name and params
def get_classifier(classifier_name, params):
    clf = None
    if classifier_name == 'SVM':
        clf = SVC(C=params['C'])
    elif classifier_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=1234)
    return clf

# Ab is function ko bula lay gayn or clf variable k equal rakh layn gay
clf = get_classifier(classifier_name, params)

# Hum apne dataset ko test and train data mein split kar lenge by 80/20 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Ab humne apne classifier ko train karna hai
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model ka accuracy score check kar lenge or isay app pe print kar denge
acc = accuracy_score(y_test, y_pred)
st.write(f'Classifier = {classifier_name}')
st.write(f'Accuracy =', acc)

#### PLOT DATASET ####
# Ab hum apne sare features ko 2 dimensional plot pe draw karenge using PCA
pca = PCA(2)
X_projected = pca.fit_transform(X)

# Ab hum apna data 0 or 1 dimension mein slice kar denge
x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

# plt.show()
st.pyplot(fig)