import cv2
import pytesseract
import numpy as np

# ✅ Set the Tesseract path (change if yours is different)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract 178 EEG signal values from image
def extract_values_from_image(image_path):
    img = cv2.imread(image_path)

    # Convert to grayscale for better OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Optional: Apply thresholding to improve OCR
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # OCR to extract text
    text = pytesseract.image_to_string(gray)

    # Extract numeric values from text
    values = [float(x) for x in text.replace(',', ' ').split() if x.replace('.', '', 1).isdigit()]
    return np.array(values[:178])  # Use only the first 178 values
