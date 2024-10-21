# Logger Module
import logging

class InteractionLogger:
    def __init__(self):
        logging.basicConfig(filename='logs/interactions.log', level=logging.INFO)

    def log(self, data):
        logging.info(data)
