import PyPDF2

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, "rb") as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate over each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page and print it
            print(page.extract_text())

# Replace 'your_file_path.pdf' with the path to your PDF file
read_pdf("PitchLetter.pdf")
