import PyPDF2
import tiktoken


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:        # extracts text from individual pages of the PDF and stores it in one large chunk
            text += page.extract_text()     
    return text


# Function to count tokens in the given text (returns the number of tokens as an integer)
def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)   # gets the encoding of model used to count tokens
    return len(encoding.encode(text))       # uses retrieved encoding to encode the text into tokens 