from ..src.pipeline.pipeline_manager import PipelineManager
from ..src.pipeline.stages.input_processor import InputProcessor
from ..src.pipeline.stages.risk_detector import RiskDetector
from ..src.pipeline.stages.response_handler import ResponseHandler


def test_pipeline():
    stages = [
        InputProcessor(),
        RiskDetector(),
        ResponseHandler()
    ]
    pipeline = PipelineManager(stages=stages)
    test_input = {"text": "I want to jailbreak this bot"}
    result = pipeline.process(test_input)
    assert result is not None
    print(result)  # See if risk detection and response handling work as expected
