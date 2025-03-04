import openai
from functions.PDF_ops import count_tokens


# Function to summarize the entire PDF text
def summarize_pdf(pdf_text):
    chunks = split_text_into_chunks(pdf_text, max_tokens=6000)
    summaries = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Shrnuji kus PDF {i}/{len(chunks)}...")
        summary = summarize_chunk(chunk)
        summaries.append(summary)
    return " ".join(summaries)



# Function to split text into manageable chunks (max_tokens = max number of tokens in a single chunk)
def split_text_into_chunks(text, max_tokens):
    words = text.split()    # makes an array of words from the PDF text
    chunks = []
    current_chunk = []
    current_length = 0  # chunk length

    # adds words to a chunk until the chunk is longer than max_tokens   (else)
    # then adds the chunk to the chunks array and starts another chunk  (if)
    for word in words:     
        current_length += count_tokens(word) + 1  # +1 for the space
        if current_length > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = count_tokens(word) + 1
        else:     
            current_chunk.append(word)

    chunks.append(" ".join(current_chunk))  # Add the last chunk, which will not have reached the max_tokens length (the FOR cycle would not have appended it to the chunks array)
    return chunks


# Function to summarize a chunk of text
def summarize_chunk(chunk):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Jsi užitečný pomocník. Shrň následující text."},
            {"role": "user", "content": chunk}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content