import streamlit as st
from PIL import Image

import style

st.title("Neural Style Transfer App")

img = st.sidebar.selectbox(
    'Select Image',
    ('amber.jpg', 'anne_hathaway.jpg', 'Anne Hathaway.jpg')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'udnie', 'rain_princess', 'rain_princess-cropped')
)

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output_images" + style_name + "-" + img

st.write("### Source Image: ")
image = Image.open(input_image)
st.image(image, width = 400)

clicked = st.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image: ")
    image = Image.open(output_image)
    st.image(image, width=400)
