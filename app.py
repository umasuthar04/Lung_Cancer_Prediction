# app.py

import streamlit as st
import pandas as pd
from PIL import Image
import random

st.set_page_config(page_title="Cancer Detection App")

# Title
st.title("🧬 Cancer Detection App")

# Sidebar
st.sidebar.header("User Input")
number = st.sidebar.slider("Select a number", 1, 100, 50)

# Main content
st.subheader("Your Number & Square")
st.write(f"**Number:** {number}")
st.write(f"**Square:** {number**2}")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV or Image file", type=["csv", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.subheader("Uploaded CSV Data")
        st.dataframe(df)

    elif uploaded_file.name.lower().endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(uploaded_file)
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)
        st.write("Image successfully uploaded!")

        # Dummy cancer prediction
        st.subheader("Prediction Result")
        prediction = random.choice(["High Risk", "Moderate Risk", "Low Risk"])
        
        icon_map = {
            "High Risk": "❗",
            "Moderate Risk": "⚠️",
            "Low Risk": "✅"
        }

        color_map = {
            "High Risk": "red",
            "Moderate Risk": "orange",
            "Low Risk": "green"
        }

        st.markdown(
            f"<h4 style='color:{color_map[prediction]}'>{icon_map[prediction]} Prediction: {prediction}</h4>",
            unsafe_allow_html=True
        )

        # Recommendation
        if prediction == "High Risk":
            st.info("Please consult an oncologist immediately.")
        elif prediction == "Moderate Risk":
            st.info("Further medical testing is recommended.")
        else:
            st.info("No major concern. Regular checkups advised.")
else:
    st.warning("Please upload a CSV or Image file to see the results.") 