import PyPDF2
import pyttsx3

def read_pdf_aloud(file_path):
    # Initialize text-to-speech engine
    tts_engine = pyttsx3.init()
    
    # Set properties to make the speech sound more natural
    # Change the rate of speech
    tts_engine.setProperty('rate', 200)  # Default is usually around 200
    
    # Select a voice (optional, depends on the available voices in your system)
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if 'en_US' in voice.languages:  # You might need to adjust the language code
            tts_engine.setProperty('voice', voice.id)
            break

    # Open the PDF file
    with open(file_path, "rb") as file:
        # Create PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate over each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page
            text = page.extract_text()
            if text:
                # Process text to replace unwanted characters or formatting issues
                text = text.replace('-\n', '')  # Remove hyphenation
                text = text.replace('\n', ' ')  # Replace new lines with spaces

                # Speak the text
                tts_engine.say(text)
                tts_engine.runAndWait()

read_pdf_aloud("OS Concepts-System Structures-Ch2.pdf")
