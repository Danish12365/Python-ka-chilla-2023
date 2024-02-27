import streamlit as st
from streamlit_embedcode import github_gist
link = "https://gist.github.com/Danish12365/adf4c069808f17118730613996e84cc6"

st.write("Embed github_gist")
github_gist(link)