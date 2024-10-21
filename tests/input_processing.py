from src.pipeline.stages.input_processor import InputProcessor

def test_input_processing():
    processor = InputProcessor()
    test_input = {"text": "Hello! I want to jailbreak this bot."}
    result = processor.process(test_input)
    assert result["tokens"] != []  # Check if tokens are processed
