import os
from PANCorpus import verificationcase

class PANCorpus:
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.corpus_id = os.path.basename(corpus_path)
        self.verification_cases = self.construct_verification_cases()
        self.answers = self.construct_answers()

    def __str__(self):
        return f'ID: "{self.corpus_id}" | Verification cases: {len(self.verification_cases)} | Distribution of Y/N-cases: {list(self.answers.values()).count("Y")}/{list(self.answers.values()).count("N")}'

    def __repr__(self):
        return self.__str__()

    def construct_answers(self):
        """Constructs a dictionary with {caseID : answer}, given there is a truth.txt or answers.txt within [corpusPath]"""
        answers = {}
        truth_filepath = ""
        if os.path.exists(self.corpus_path + "\\truth.txt"): truth_filepath = self.corpus_path + "\\truth.txt"
        elif os.path.exists(self.corpus_path + "\\answers.txt"): truth_filepath = self.corpus_path + "\\answers.txt"

        with open(truth_filepath, 'r', encoding='utf-8') as answer_lines:
            for answer_line in answer_lines:
                last_space_index = answer_line.rfind(" ")
                case_id = answer_line[:last_space_index].strip().replace(u'\ufeff', '')
                answer = answer_line[last_space_index:].strip().replace(u'\ufeff', '')
                answers.update({case_id: answer})
        return answers

    def construct_verification_cases(self):
        verification_cases = []
        for case_id in os.listdir(self.corpus_path):
            if os.path.isdir(os.path.join(self.corpus_path, case_id)):
                verification_cases.append(verificationcase.VerificationCase(self.corpus_path + "\\" + case_id))
        return verification_cases


# Usage:
# ---------------------------------------------
# pan_corpus = PANCorpus("PATH_TO_PAN_CORPUS")
# from pprint import pprint
# pprint(pan_corpus.verification_cases)