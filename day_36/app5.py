import pandas as pd 
import pandas_profiling
import streamlit as st
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report
from pydantic_settings import BaseSettings 

df = sns.load_dataset("titanic")
pr = df.profile_report()

st_profile_report(pr)