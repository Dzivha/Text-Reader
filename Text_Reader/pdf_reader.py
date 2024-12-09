import PyPDF2
import pyttsx3

def read_pdf_aloud(file_path):
    # Initialize text-to-speech engine
    tts_engine = pyttsx3.init()
    
    # Open the PDF file
    with open(file_path, "rb") as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate over each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page
            text = page.extract_text()
            if text:
                # Speak the text
                tts_engine.say(text)
                tts_engine.runAndWait()


read_pdf_aloud("PitchLetter.pdf")
