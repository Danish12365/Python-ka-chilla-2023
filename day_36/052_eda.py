import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from pydantic import BaseModel, BaseSettings, Field, PrivateAttr
from pydantic_settings import BaseModel, BaseSettings, Field, PrivateAttr


# webapp ka title
st.markdown('''
# **Exporatory Data Analysis web Application**
This app is developed by Danish**EDA app**            
''')

# how to upload files from pc
with st.sidebar.header('Upload your dataset (.CSV)'):
     uploaded_file = st.sidebar.file_uploader("Choose a file", type=['csv'])
     df = sns.load_dataset('titanic')
     st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins.csv)")
    


# profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100, 5), columns=['a', 'b', 'c', 'd', 'e'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
