from PyPDF2 import PdfReader
import re
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


class PDFTextExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)
    
    def extract_text(self):
        text = ""
        for page_num in range(len(self.reader.pages)):
            page = self.reader.pages[page_num]
            text += page.extract_text()
        return text
    
    def split_into_sections_and_chapters(self):
        # Extract text from the PDF
        text = self.extract_text()

        # Define regular expressions to identify sections and chapters
        section_pattern = re.compile(r'Section \d+\s+.+')
        chapter_pattern = re.compile(r'Chapter \d+\s+.+')

        sections = section_pattern.split(text)
        sections_titles = section_pattern.findall(text)

        sections_with_chapters = []

        for i, section in enumerate(sections):
            if i == 0:
                continue  # Skip first section

            chapters = chapter_pattern.split(section)
            chapter_titles = chapter_pattern.findall(section)
            
            chapters_with_content = []
            for j in range(len(chapter_titles)):
                if j + 1 < len(chapters):
                    chapters_with_content.append((chapter_titles[j], chapters[j + 1]))
                else:
                    chapters_with_content.append((chapter_titles[j], chapters[j]))

            sections_with_chapters.append((sections_titles[i - 1], chapters_with_content))
        
        return sections_with_chapters
    
    
    

