# TajStone AI - Taj Mahal Stone Deterioration Detection
import streamlit as st
from PIL import Image

st.set_page_config(page_title="TajStone AI", page_icon="🕌")

st.title("🕌 TajStone AI")
st.subheader("AI for Taj Mahal Preservation")

st.write("Upload a stone image to detect deterioration level")

uploaded_file = st.file_uploader("Choose stone image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Demo logic - replace with your ML model later
    st.warning("Analysis Result:")
    st.write("**Condition:** Moderate Weathering Detected")
    st.write("**Confidence:** 87%")
    st.write("**Recommendation:** Conservation needed")
    st.progress(87)
    
else:
    st.info("Please upload an image to start analysis")

st.sidebar.header("About Project")
st.sidebar.write("Built for Taj Mahal Preservation Hackathon")
st.sidebar.write("Tech: Python, Streamlit, AI Image Processing")
