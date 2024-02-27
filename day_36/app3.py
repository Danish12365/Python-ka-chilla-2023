import streamlit as st 
from PIL import Image

st.write(""" # add midea files in streamlit web_app 
""")

# add Image
st.write("""
## image""")
image1 = Image.open("snowleopard.jpg") 
st.image(image1)
# add video
st.write("""
## video""")

video1 = open("leo.mp4", "rb")
st.video (video1)

# add audio
st.write("""
## Audio""")

audio1 = open("leo.mp3", "rb")
st.audio (audio1)
