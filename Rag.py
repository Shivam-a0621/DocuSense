from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

class QAHandler:
    def __init__(self, model_name='llama3-70b-8192', api_key=None):
        self.text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len,
        )
        self.embeddings = HuggingFaceEmbeddings()
        self.chat = ChatGroq(
            temperature=0,
            model=model_name,
            api_key=api_key
        )
        self.vectorstore = None  # Initialize vectorstore to None

    def preprocess_text(self, text):
        splitted_text = self.text_splitter.split_text(text)
        self.vectorstore = FAISS.from_texts(splitted_text, self.embeddings)
        self.vectorstore.save_local("vector_index")
        
    
    def perform_qa(self, query):
        
        self.db= FAISS.load_local("vector_index", self.embeddings, allow_dangerous_deserialization=True)
        retriever = self.db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        rqa = RetrievalQA.from_chain_type(llm=self.chat, chain_type="stuff", retriever=retriever, return_source_documents=True)
        result = rqa.invoke(query)
        return result['result']
