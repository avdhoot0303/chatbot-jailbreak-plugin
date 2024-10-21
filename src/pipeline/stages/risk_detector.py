# Risk Detector Module
from transformers import BertTokenizer, BertForSequenceClassification
import torch

class RiskDetector:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    def detect_risk(self, input_data):
        inputs = self.tokenizer(input_data['text'], return_tensors="pt", padding=True, truncation=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        risk_score = torch.softmax(logits, dim=1)[0][1].item()  # Probability of "risky"
        return {"risk_score": risk_score, "risky": risk_score > 0.5}
