from flask import Flask, request, jsonify
import pdfplumber
from flask import Flask, render_template, redirect, url_for
import os

import google.generativeai as genai
from apikey import key
import json

genai.configure(api_key=key) # Create the model
generation_config = {
  "temperature": 0.95,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

app = Flask(__name__) # Folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Allowed file extensions for upload
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg',}  # Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS     #pdf plumber
def extract_text_with_layout(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()  # This extracts text with layout
    return text     # API route to handle file upload and text extraction
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):        # Extract text from the uploaded PDF
        extracted_text = extract_text_with_layout(file)
        return jsonify({'text': extracted_text}), 200
    
    return jsonify({'error': 'Invalid file format. Please upload a PDF.'}), 400

@app.route('/', methods=['GET', 'POST'])
def home():
    content = ''
    if request.method == "POST":        # Check if a file was uploaded
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']

        # Check if the user has not selected a file
        if file.filename == '':
            return "No selected file"
        
        # Validate the file extension
        if file and allowed_file(file.filename):
            # Secure the filename and save it in the upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Return the file path as confirmation
            content = f"{extract_text_with_layout(file_path)}"
            # content = model.generate_content([extract_text_with_layout(file_path)])
            # json_content = json.loads(content)
            # print

    
    return render_template('upload_form.html', content=content)


if __name__ == '__main__':
    app.run(debug=True,port=8000)
    