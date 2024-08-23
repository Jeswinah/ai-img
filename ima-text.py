import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
headers = {"Authorization": "Bearer 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"}

def query(image_data):
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()

# Streamlit app
st.title("Handwritten Text Recognition")

uploaded_file = st.file_uploader("Upload an image", type="jpg")
if uploaded_file is not None:
    if st.button("Search"):
        image_data = uploaded_file.read()  # Read the uploaded file as bytes
        output = query(image_data)  # Pass the image data to the API
        st.write(output)  # Display the output from the API
