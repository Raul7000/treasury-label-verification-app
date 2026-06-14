from flask import Flask, render_template, request, send_from_directory
import os
import pytesseract
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        file = request.files['label_image']

        if file.filename != '':

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(filepath)

            image = Image.open(filepath)

            extracted_text = pytesseract.image_to_string(image)
            verification_results = ""

        if ("government warning" in extracted_text.lower()
            or "should not" in extracted_text.lower()
            or "birth defects" in extracted_text.lower()):
            verification_results += "✓ Government Warning Found<br>"
        else:
            verification_results += "✗ Government Warning Missing<br>"

            
          
        if "750" in extracted_text:
            verification_results += "✓ Net Contents Found<br>"

        if "product of japan" in extracted_text.lower():
            verification_results += "✓ Country of Origin Found<br>"

        return f"""
        <h1>File uploaded successfully!</h1>

        <p>{file.filename}</p>

        <img src="/uploads/{file.filename}" width="400">

        <h2>Verification Results</h2>

        <p>{verification_results}</p>

        <h2>Extracted Text</h2>

        <pre>{extracted_text}</pre>
        """


    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)