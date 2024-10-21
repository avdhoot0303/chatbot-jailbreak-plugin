# Input Processor Module
import spacy

class InputProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, input_data):
        doc = self.nlp(input_data['text'])
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return {"tokens": tokens, "text": input_data['text']}
