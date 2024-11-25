from flask import Flask, request, jsonify
import pdfplumber

app = Flask(__name__)

                                # Function to extract text from PDF using pypdf2

                                            #pdf plumber
def extract_text_with_layout(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()  # This extracts text with layout
    return text

# API route to handle file upload and text extraction
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        extracted_text = extract_text_with_layout(file)
        return jsonify({'text': extracted_text}), 200

    return jsonify({'error': 'Invalid file format. Please upload a PDF.'}), 400


if __name__ == '__main__':
    app.run(debug=True)
