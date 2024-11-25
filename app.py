from flask import Flask, request, render_template, redirect, url_for
import os
from PDF2T import extract_text_with_layout as pdf2t

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed file extensions for upload
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg',}

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    content= ''
    if request.method == "POST":
        # Check if a file was uploaded
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
            content = f"{pdf2t(file_path)}"
    
    # Render the file upload form
    return render_template('upload_form.html', content=content)

if __name__ == "__main__":
    app.run(debug=True,port=8088)
