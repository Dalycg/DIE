# Document Insight Extractor

**Project Overview**:
Document Insight Extractor is a Python-based application designed to extract and summarize essential information from PDF documents. The tool leverages advanced natural language processing (NLP) techniques powered by OpenAI's GPT model to provide comprehensive, structured, and clear summaries of document content, preserving the original language and ensuring professional presentation.

**Key Features**:
- **PDF Text Extraction**: The tool reads and processes the content of PDF files, efficiently extracting the text for further analysis.
- **Automated Summarization**: Using the GPT model, the extracted text is summarized, highlighting key points, significant details, and providing an overall summary of the document.
- **Language Retention**: Summaries are generated in the same language as the original document, ensuring accuracy and context preservation.
- **Professional Output**: The summary is structured and formatted to be clear, legible, and suitable for professional use.

**Use Cases**:
- Ideal for professionals who need to quickly review and understand large documents.
- Useful in scenarios where a quick and accurate summary is needed without losing critical information.
- Can be integrated into workflows requiring automated document processing and summarization.

**Technology Stack**:
- Python for the core application.
- Pdfplumber for PDF text extraction.
- OpenAI's GPT model for natural language processing and summarization.
- FastAPI for building the API.
- Uvicorn as the ASGI server to serve the FastAPI application.

**API Documentation**:
- The API comes with built-in documentation using **Swagger** and **ReDoc**. You can access the Swagger UI documentation at `http://localhost:8000/docs` and the ReDoc documentation at `http://localhost:8000/redoc`.

**Running the Application**:
To start the API server, follow these steps:

1. Ensure all dependencies are installed.
2. Run the application using the following command:
   python DIE.py or py DIE.py

3. The server will start on `localhost` at port `8000`.


