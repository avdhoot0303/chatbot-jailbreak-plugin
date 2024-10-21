from src.pipeline.stages.input_processor import InputProcessor

def test_input_processing():
    processor = InputProcessor()
    test_input = {"text": "I want to jailbreak this chatbot!"}
    result = processor.process(test_input)
    assert isinstance(result["tokens"], list)  # Ensure tokens are in list format
    assert "jailbreak" in result["tokens"]  # Ensure important words are included
    assert "I" not in result["tokens"]  # Ensure stopwords are removed
    print(result)
