#install openai, tiktoken, PyPDF2

import openai
from functions.chatbot import chatbot_with_pdf

# Initialize OpenAI API key
openai.api_key = "OpenAI_API_key"
pdf_path = r"path_to_pdf"

chatbot_with_pdf(pdf_path)