import uuid
from preprocess import PDFTextExtractor

class TreeNode:
    def __init__(self, title, content=None, level=0):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content if content else []
        self.level = level
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode(id={self.id}, title={self.title}, level={self.level}, children={len(self.children)})"

class BookParser:
    def __init__(self, file_path):
        self.extractor = PDFTextExtractor(file_path)
        self.tree_root = None
    
    def parse_book_content(self, book_content):
        lines = book_content.split('\n')
        root = TreeNode("Textbook")
        current_section = None
        current_chapter = None

        for line in lines:
            line = line.strip()
            if line.startswith("Section"):
                current_section = TreeNode(line, level=1)
                root.add_child(current_section)
                current_chapter = None
            elif line.startswith("Chapter"):
                current_chapter = TreeNode(line, level=2)
                if current_section:
                    current_section.add_child(current_chapter)
            elif current_chapter and line:
                current_chapter.content.append(line)
        
        self.tree_root = root
        return root

    def print_tree(self, node=None, indent=0):
        if node is None:
            node = self.tree_root
        if node is None:
            return ""
        
        tree_str = "  " * indent + f"{node.title} (ID: {node.id})\n"
        for child in node.children:
            tree_str += self.print_tree(child, indent + 1)
        
        return tree_str

    def read_and_parse(self):
        # Extract text from the PDF
        book_content = self.extractor.extract_text()
        # Parse the content into a tree structure
        self.parse_book_content(book_content)

# Example usage:
# parser = BookParser("path_to_your_pdf.pdf")
# parser.read_and_parse()
# print(parser.print_tree())

