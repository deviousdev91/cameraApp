import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")
st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if uploaded_image:
    st.markdown("<b>Image</b>", unsafe_allow_html=True)
    st.image(uploaded_image)
    st.markdown("<b>Grayscale Image</b>", unsafe_allow_html=True)
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)

#Render grayscale image on the webpage

