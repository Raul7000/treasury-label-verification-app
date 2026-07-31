from flask import Flask, render_template, request, send_from_directory
import os
import pytesseract
from PIL import Image, ImageOps

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        file = request.files['label_image']

        if file.filename != '':

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(filepath)

            image = Image.open(filepath)
            image = ImageOps.exif_transpose(image)

            extracted_text = pytesseract.image_to_string(image)
            verification_results = ""
            text = extracted_text.lower()
            
            
            if ("government warning" in text
               or "should not" in text
               or "birth defects" in text):
                verification_results += "✓ Government Warning Found\n"
            else:
                verification_results += "✗ Government Warning Missing\n"
            
                       
            net_contents = [
                "50 ml", "50ml",
                "200 ml", "200ml",
                "375 ml", "375ml",
                "500 ml", "500ml",
                "720 ml", "720ml",
                "750 ml", "750ml", "750m!",
                "1 l", "1l",
                "1.75 l", "1.75l"
            ]

            if any(size in text for size in net_contents):
                verification_results += "✓ Net Contents Found\n"
            else:
                verification_results += "✗ Net Contents Missing\n"

            if "product of japan" in text or "japan" in text:
                verification_results += "✓ Country of Origin Found\n"
            else:
                verification_results += "✗ Country of Origin Missing\n"

            return render_template(
                "index.html",
                filename=file.filename,
                verification_results=verification_results,
                extracted_text=extracted_text
            )


    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)