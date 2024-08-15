import openai
import string
from PyPDF2 import PdfReader

# Set up API key
openai.api_key = ""

def extract_text_from_pdf(pdf_file):

    # Read the content of the PDF file as a string
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # Remove unnecessary whitespace
    text = ' '.join(text.split())

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

def summarize_pdf(pdf_file):

    # Read the content of the PDF file
    pdf_data = extract_text_from_pdf(pdf_file)

    prompt = (
    "Your task is to act as a Document Insight Extractor. "
    "You will receive text extracted from a PDF document, and your objective is to extract and summarize all essential information from it. "
    "The summary should be comprehensive, covering key points, significant details, and providing an overall clear and structured overview of the document's content. "
    "Please ensure that the summary retains the language of the original document and is presented in a professional and legible manner. "
    "Begin by reviewing the document, and then provide the summarized content in the language of the document below.\n\n"
    f"Document text: {pdf_data}"
    )

    # Call the OpenAI API to summarize the content of the PDF
    response = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": "You are a document insight extractor."},
            {"role": "user", "content": prompt},
        ]
            
    )

    return response.choices[0].message.content


pdf_file_path = "./COMMERCIAL INVOICE-SM242686.pdf"


summary = summarize_pdf(pdf_file_path)  
print(summary)



