import streamlit as st
import numpy as np
import joblib
from utils.ocr import extract_values_from_image
from utils.report_gen import generate_pdf
from chatbot.gemini_chat import ask_gemini

st.set_page_config(page_title="EEG Seizure Detection System")
st.title("🧠 Real-time Epileptic Seizure Detection System")

# Upload EEG report image
image = st.file_uploader("Upload your EEG report image", type=["jpg", "png", "jpeg"])

if image:
    st.image(image, caption="Uploaded EEG Image", use_column_width=True)

    # Save temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(image.read())

    # Extract EEG signal
    signals = extract_values_from_image("temp_image.jpg")

    if len(signals) == 178:
        model = joblib.load("model/best_model.pkl")
        prediction = model.predict([signals])[0]
        confidence = max(model.predict_proba([signals])[0])

        st.success(f"Prediction: {'SEIZURE' if prediction == 1 else 'NON-SEIZURE'}")
        st.info(f"Model Confidence: {confidence:.2f}")

        # Ask Gemini for explanations
        explanation = ask_gemini(f"Explain what a {prediction} prediction means in an EEG report.")
        measures = ask_gemini("What precautions should a seizure-prone person take?")
        medicine = ask_gemini("Suggest medicines for epilepsy.")

        # Generate PDF Report
        if st.button("Generate PDF Report"):
            generate_pdf(prediction, confidence, measures, medicine)
            with open("report.pdf", "rb") as pdf_file:
                st.download_button(label="Download PDF", data=pdf_file, file_name="EEG_Report.pdf")

        # Chat with Gemini
        st.subheader("💬 Ask the AI Doctor")
        user_input = st.text_input("Ask about your EEG result or seizures:")
        if user_input:
            response = ask_gemini(user_input)
            st.write(response)
    else:
        st.error("Failed to extract 178 EEG values. Check the image quality.")
