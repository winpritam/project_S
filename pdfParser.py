import requests
import argparse

def get_pdf_text_from_api(pdf_path=None,**kwargs):
    url = r'https://winpritam.pythonanywhere.com/extract-text'  # The URL of the Flask API

    if kwargs['file']:
        pdf_path = kwargs['file']
    
    files = {'file': open(pdf_path, 'rb')}      # Open the PDF file in binary mode

    try:
        # Send the POST request with the PDF file
        response = requests.post(url, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the extracted text from the response
            data = response.json()
            extracted_text = data.get('text', '')
            return extracted_text
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage



if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process keyword arguments.")
    # Add arguments using --key=value format
    parser.add_argument('--file', type=str, help='Path to the PDF file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert argparse Namespace to a dictionary
    kwarg = vars(args)

    pdf_path = r"D:\Downloads\Pritam_resume\Resume-Junior-AI_ML-Developer.pdf"  # Path to the PDF file you want to process
    extracted_text = get_pdf_text_from_api(pdf_path,**kwarg)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
