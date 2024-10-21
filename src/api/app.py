# FastAPI Application
from fastapi import FastAPI
from pydantic import BaseModel
from src.pipeline.pipeline_manager import PipelineManager
from src.pipeline.stages.input_processor import InputProcessor
from src.pipeline.stages.risk_detector import RiskDetector
from src.pipeline.stages.response_handler import ResponseHandler

app = FastAPI()

class ChatbotInput(BaseModel):
    text: str

stages = [
    InputProcessor(),
    RiskDetector(),
    ResponseHandler()
]
pipeline = PipelineManager(stages=stages)

@app.post("/assess/")
async def assess_risk(input_data: ChatbotInput):
    result = pipeline.process(input_data.dict())
    return result
