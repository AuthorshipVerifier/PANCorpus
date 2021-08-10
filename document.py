import os
import re

class Document:
    def __init__(self, document_path):
        self.path = document_path
        self.id = os.path.splitext(os.path.basename(document_path))[0]
        self.raw_text = self.raw_text()
        self.normalized_text = self.normalized_text()

    def raw_text(self):
        with open(self.path, 'r', encoding='utf-8') as doc:
            return doc.read()

    def normalized_text(self):
        cleaned_text = re.sub(r"[\r\n]+", " ", self.raw_text)
        cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)
        return cleaned_text
