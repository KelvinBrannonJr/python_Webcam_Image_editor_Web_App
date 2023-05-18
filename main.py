import streamlit as st
from functions import convert_image


st.subheader("Convert Color to Grayscale")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")


with st.expander("Start Camera"):
    # Enable the camera
    camera_image = st.camera_input("Camera Image")

# conditional to make sure object has data before running script
if camera_image:
    gray_camera_image = convert_image(camera_image)

    # Render the grayscale image on the webpage
    st.image(gray_camera_image)

# Converter for uploading image from an external file
if uploaded_image:
    gray_uploaded_image = convert_image(uploaded_image)
    st.image(gray_uploaded_image)
