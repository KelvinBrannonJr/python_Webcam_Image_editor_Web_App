import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # Enable the camera
    camera_image = st.camera_input("Camera Image")

# conditional to make sure object has data before running script
if camera_image:

    # Create image instance using 'Pillow' module
    img = Image.open(camera_image)

    # Convert image instance into grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)


