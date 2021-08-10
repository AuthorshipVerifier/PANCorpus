import os
import re
from PANCorpus import document

class VerificationCase:
    def __init__(self, problem_filepath):
        self.filepath = problem_filepath
        self.id = os.path.basename(self.filepath)
        self.knowns_filepaths = self.enum_documents()[0]
        self.unknown_filepath = self.enum_documents()[1]
        self.knowns = self.knowns()
        self.known_concatenated = self.known_concatenated()
        self.unknown = self.unknown()

    def __str__(self):
        return f'ID: "{self.id}" | Number of known docs: {len(self.knowns)}'

    def __repr__(self):
        return self.__str__()

    def enum_documents(self):
        knowns_filepaths = []
        unknown_filepath = ""
        basePath = self.filepath + "\\"
        for doc_path in os.listdir(self.filepath):
            if doc_path.startswith("known"):
                knowns_filepaths.append(basePath + doc_path)
            elif doc_path.startswith("unknown"):
                unknown_filepath = basePath + doc_path
        return knowns_filepaths, unknown_filepath

    def knowns(self):
        known_docs = []
        for known_filepath in self.knowns_filepaths:
            known_docs.append(document.Document(known_filepath))
        return known_docs

    def unknown(self):
        return document.Document(self.unknown_filepath).normalized_text

    def known_concatenated(self):
        concat_known_doc = ""
        for known in self.knowns:
            concat_known_doc += " " + known.normalized_text
        return re.sub(r"\s{2,}", " ", concat_known_doc)


