import gradio as gr
from preprocess import PDFTextExtractor
from heirarchial_structure import BookParser  # Assuming you saved the TreeNode and BookParser in tree_parser.py
from Biencoder import Bi_Encoder  # Assuming you saved the Bi_Encoder class in bi_encoder.py
from Rag import QAHandler
from sentence_transformers import SentenceTransformer



# Load models for the chatbot
bi_encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize QAHandler with appropriate model and API key
qa_handler = QAHandler(model_name='llama3-70b-8192', api_key="")

# Function to save the uploaded PDF file
def save_pdf(file):
    with open("uploaded_file.pdf", "wb") as f:
        f.write(file.read())
    return "PDF saved successfully!"

# Function to preprocess the PDF file
def preprocess_pdf(file):
    extractor = PDFTextExtractor(file.name)
    text = extractor.extract_text()
    
    with open("preprocessed_text.txt", "w", encoding='utf-8') as f:
        f.write(text)
    print("before rag")    
    qa_handler.preprocess_text(text)
    print("after rag")
    return "PDF preprocessed and text indexed successfully!"

# Function to read text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to handle chatbot queries using bi-encoder retrieval
def chatbot_bi_encoder(query, k_top):
    bi_encoder_instance = Bi_Encoder("preprocessed_text.txt", query, k_top)
    bi_encoder_instance.chatbot_bi_encoder()
    results = bi_encoder_instance.semantic_search()
    return results

# Function to display hierarchical tree
def display_tree():
    parser = BookParser("preprocessed_text.txt")
    parser.read_and_parse()
    return parser.print_tree()

# Switchable chatbot function
def chatbot(query, mode, slider):
    if mode == "QA_RAG":
        return qa_handler.perform_qa(query)
    elif mode == "Bi-Encoder":
        results = chatbot_bi_encoder(query, slider)
        return results
    elif mode == "Hierarchical Structure":
        return display_tree()

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## PDF Processing and Chatbot Interface")
    
    # PDF Upload and Display
    pdf_file = gr.File(label="Upload PDF", file_types=[".pdf"])
    save_button = gr.Button("Save PDF")
    
    save_button.click(save_pdf, inputs=pdf_file, outputs=None)
    
    # Preprocess PDF
    preprocess_button = gr.Button("Preprocess PDF")
    preprocess_button.click(preprocess_pdf, inputs=pdf_file, outputs=None)
    
    # Chatbot
    chatbot_input = gr.Textbox(label="Enter your query")
    mode_selector = gr.Radio(["QA_RAG", "Bi-Encoder", "Hierarchical Structure"], label="Select Chatbot Mode", value="QA_RAG")
    slider_input = gr.Slider(label="K", minimum=1, maximum=3, step=1)
    chatbot_button = gr.Button("Get Response")
    
    chatbot_output = gr.Textbox(label="Response")
    
    chatbot_button.click(chatbot, inputs=[chatbot_input, mode_selector, slider_input], outputs=chatbot_output)

# Launch the interface
demo.launch()
