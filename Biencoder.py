from sentence_transformers import SentenceTransformer, util
from preprocess import PDFTextExtractor

bi_encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class Bi_Encoder:
    def __init__(self, file_path, query, k):
        self.model = bi_encoder
        self.query = query
        self.k = k
        self.extractor = PDFTextExtractor(file_path)
        self.encoded_sections = []

    def chatbot_bi_encoder(self):
        sections_with_chapters = self.extractor.split_into_sections_and_chapters()
        
        # Encode sections and chapters
        for section_title, chapters in sections_with_chapters:
            for chapter_title, chapter_content in chapters:
                encoded_content = self.model.encode(chapter_content, convert_to_tensor=True)
                self.encoded_sections.append((section_title, chapter_title, chapter_content, encoded_content))
        
        return self.encoded_sections
    
    def semantic_search(self):
        # Encode the query
        query_embedding = self.model.encode(self.query, convert_to_tensor=True)
        
        # Collect all embeddings and their associated titles and contents
        all_embeddings = [item[3] for item in self.encoded_sections]
        all_titles = [(item[0], item[1]) for item in self.encoded_sections]
        all_contents = [item[2] for item in self.encoded_sections]
        
        # Perform semantic search
        hits = util.semantic_search(query_embedding, all_embeddings, top_k=self.k)[0]
        
        # Collect results
        results = [((all_titles[hit['corpus_id']][0], all_titles[hit['corpus_id']][1], all_contents[hit['corpus_id']]), hit['score']) for hit in hits]
        return results


