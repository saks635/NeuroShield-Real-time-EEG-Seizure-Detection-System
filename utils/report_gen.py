from fpdf import FPDF
from datetime import datetime

def generate_pdf(prediction, confidence, measures, medicine, filename='report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Epileptic Seizure Detection Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    # Results
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Prediction: {'SEIZURE' if prediction == 1 else 'NON-SEIZURE'}", ln=True)
    pdf.cell(200, 10, txt=f"Model Confidence: {confidence:.2f}", ln=True)

    # Precautions and Medicine
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Precautionary Measures:\n{measures}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Suggested Medications:\n{medicine}")

    pdf.output(filename)
