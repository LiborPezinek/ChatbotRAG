import openai
from functions.summary import summarize_pdf
from functions.PDF_ops import extract_text_from_pdf, count_tokens

# Chatbot function
def chatbot_with_pdf(pdf_path):
    # Extract text from the provided PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # counts tokens in original PDF
    token_count = count_tokens(pdf_text)
    print(f"Počet tokenů původního PDF: {token_count}")

    # Summarize the content if token count exceeds limit
    if token_count > 8000:
        print("Dokument je příliž velký a bude shrnut...")
        pdf_text = summarize_pdf(pdf_text)
        print("Shrnování dokončeno")
        
        # counts tokens in summarized PDF
        token_count = count_tokens(pdf_text)
        print(f"Počet tokenů shrnutého PDF: {token_count}")
    
    print("\n--- Chatbot připraven ---")
    print("K ukončení chatu zadejte 'konec'\n")


    # Start chat loop
    while True:
        user_input = input("Prompt: ")
        if user_input.lower() == 'konec':
            print("Chatbot: Nashledanou")
            break

        # Generate response using OpenAI
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Jsi užitečný pomocník. Použij informace ze shrnutého PDF k zodpovězení otázek."},
                {"role": "user", "content": f"Toto je shrnutý text z PDF:\n\n{pdf_text}\n\nOtázka uživatele: {user_input}"}
            ],
            temperature=0.2
        )
        chatbot_reply = response.choices[0].message.content
        print(f"Chatbot: {chatbot_reply}")