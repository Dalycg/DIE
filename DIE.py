import openai
import pdfplumber
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn


# Set up API key


app = FastAPI(
    title="Document Insights Extractor API",
    description="An API for extracting and summarizing text from PDF documents.",
    version="1.0.0",
    docs_url="/docs",  # Make sure this is set correctly
    redoc_url="/redoc",  # Redoc URL
)

def extract_text_from_pdf(file):
    try:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        text = ' '.join(text.split())
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the PDF: {str(e)}")


@app.post(
    "/summarize/",
    summary="Summarize a PDF document",
    description=(
        "Uploads a PDF file and provides a summary of its content. "
        "The summary is generated using OpenAI's GPT model, which processes the extracted text from the PDF. "
        "Ensure that the uploaded file is a valid PDF document. "
        "The response will include a summary of the key points and details from the document."
    ),
    tags=["PDF Processing"],
    responses={
        200: {"description": "Successfully summarized the PDF document.", "content": {"application/json": {}}},
        400: {"description": "The uploaded file is not a valid PDF or there was an error processing the file."},
        500: {"description": "An error occurred while interacting with OpenAI API or processing the PDF."}
    }
)
async def summarize_pdf(file: UploadFile = File(...)):
    """
    Summarize a PDF Document

    - **file**: The PDF file to be summarized. Must be of type `application/pdf`.

    Returns a JSON object containing the summary of the PDF document.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="The uploaded file is not a PDF.")

    try:
        pdf_data = extract_text_from_pdf(file.file)
    except HTTPException as e:
        raise e  # Re-raise any HTTPException already handled in extract_text_from_pdf

    prompt = (
    "Your task is to act as a Document Insight Extractor. "
    "You will receive text extracted from a PDF document, and your objective is to extract and summarize all essential information from it. "
    "The summary should be comprehensive, covering key points, significant details, and providing an overall clear and structured overview of the document's content. "
    "Please ensure that the summary retains the language of the original document and is presented in a professional and legible manner. "
    "Begin by reviewing the document, and then provide the summarized content in the language of the document below.\n\n"
    f"Document text: {pdf_data}"
    )
    try:
        # Call the OpenAI API to summarize the content of the PDF
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": "You are a document insight extractor."},
                {"role": "user", "content": prompt},
            ]
            
        )
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"Error interacting with OpenAI API: {str(e)}")

    summary= response.choices[0].message.content

    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




