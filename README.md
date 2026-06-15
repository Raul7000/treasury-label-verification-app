AI-Powered Alcohol Label Verification Prototype
Overview

This project is a prototype web application developed for the U.S. Department of the Treasury take-home assessment.

The application allows a user to upload an image of an alcohol label, performs Optical Character Recognition (OCR) on the image, and verifies whether required compliance language is present.

Approach

This prototype demonstrates how Optical Character Recognition (OCR) can assist Treasury compliance agents by automatically extracting text from alcohol beverage labels and verifying selected compliance-related information.
The application accepts uploaded label images, extracts text using Tesseract OCR, and evaluates the extracted text against selected compliance checks.
Results are displayed to the user along with the extracted text for review.

Features
Upload alcohol label images
Extract text using Tesseract OCR
Display uploaded image
Display extracted text
Verify presence of required warning language
Display compliance verification results
Technologies Used
Python 3
Flask
Tesseract OCR
Pillow (PIL)
HTML
GitHub
Installation
Clone the repository:
git clone https://github.com/Raul7000/treasury-label-verification-app.git
Install required packages:
pip install -r requirements.txt
Install Tesseract OCR and ensure it is available in the system PATH.
Running the Application

Start the Flask application:

python app.py

Open a browser and navigate to:

http://127.0.0.1:5000
Verification Logic

The prototype performs OCR on uploaded label images and searches for phrases associated with required alcohol warning statements.

Examples include:

Government Warning
Should Not Drink
Birth Defects

Verification results are displayed to the user after processing.

Assumptions and Limitations
OCR accuracy depends on image quality.
Blurry or poorly lit images may reduce text recognition accuracy.
This prototype demonstrates proof-of-concept functionality and is not intended for production use.
Additional compliance rules could be added in future iterations.
Repository

GitHub Repository:

https://github.com/Raul7000/treasury-label-verification-app

Deployed Application

https://treasury-label-verification-app.onrender.com




