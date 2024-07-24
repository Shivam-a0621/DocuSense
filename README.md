# DocuSense: Intelligent Document Processing and Chatbot Interface

**DocuSense** is a powerful application designed for extracting text from PDF documents, performing semantic searches using a bi-encoder, and visualizing hierarchical document structures. The app provides a user-friendly interface for interacting with documents and retrieving information efficiently.

## Project Overview

**DocuSense** integrates several advanced technologies to handle documents:

- **PDF Text Extraction**: Extracts and preprocesses text from PDF files.
- **Semantic Search**: Uses bi-encoder models to perform intelligent searches over document content.
- **Hierarchical Visualization**: Parses and displays document structures, such as sections and chapters, in a hierarchical format.

## Features

- **Text Extraction**: Extract text from PDF files and preprocess it for further analysis.
- **Bi-Encoder Retrieval**: Perform semantic search queries using a bi-encoder model to retrieve relevant content.
- **Hierarchical Structure Visualization**: Display the hierarchical structure of documents, including sections and chapters.

## Screenshots

1. **QA Output**:
    ![QA Output](https://github.com/Shivam-a0621/DocuSense/blob/master/img_vid/Screenshot%202024-07-25%20042919.png)

2. **Bi-Encoder Output**:
    ![Bi-Encoder Output](https://github.com/Shivam-a0621/DocuSense/blob/master/img_vid/Screenshot%202024-07-25%20042943.png)

3. **Hierarchical Output**:
    ![Hierarchical Output](https://github.com/Shivam-a0621/DocuSense/blob/master/img_vid/Screenshot%202024-07-25%20042919.png)

4. **SAmple Video**:
      [![Watch the video](https://github.com/Shivam-a0621/DocuSense/blob/master/Resources/Screenshot%202024-07-25%20045813.png)](https://github.com/Shivam-a0621/DocuSense/blob/master/img_vid/Gradio%20-%20Google%20Chrome%202024-07-25%2004-27-17.mp4)
       

## Requirements

- Python 3.7+
- PyPDF2
- SentenceTransformers
- LangChain
- gradio
- (Additional libraries as required)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:

    ```bash
    python app.py
    ```

    This will launch the Gradio interface where you can upload PDF files, preprocess them, and interact with the chatbot.

2. **Upload a PDF**:
    - Use the "Upload PDF" button to upload your PDF file.
    - Click "Save PDF" to save the file.
    - Click "Preprocess PDF" to extract and preprocess the text.

3. **Interact with the Chatbot**:
    - Enter your query in the "Enter your query" textbox.
    - Select the chatbot mode:
        - **QA**: Uses Retrieval-Augmented Generation (RAG) for answering questions.
        - **Bi-Encoder**: Uses a bi-encoder model for semantic search.
        - **Hierarchical Structure**: Displays the hierarchical structure of the document.
    - Click "Get Response" to see the results.

## Code Explanation

- **PDFTextExtractor**: Handles text extraction from PDF files and preprocessing.
- **QAHandler**: Manages semantic search and QA functionalities using LangChain and bi-encoder models.
- **TreeNode**: Represents nodes in the hierarchical structure of documents.
- **Gradio UI**: Provides an interactive interface for users to upload documents, run queries, and view results.

## Troubleshooting

- **EOF Marker Not Found**: This error typically occurs with corrupted or incomplete PDF files. Ensure that the PDF is intact and try re-uploading.
- **Missing Dependencies**: Ensure all required libraries are installed as per the `requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [bhardwajshivam.2108@gmail.com].
