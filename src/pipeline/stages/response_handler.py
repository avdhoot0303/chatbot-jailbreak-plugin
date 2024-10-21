# Response Handler Module
class ResponseHandler:
    def handle_response(self, risk_data):
        if risk_data["risky"]:
            return {"response": "Your input may violate the chatbot's safety policies.", "escalate": True}
        else:
            return {"response": "Thank you for your input. How can I assist you further?", "escalate": False}
