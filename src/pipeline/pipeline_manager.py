# Pipeline Manager
class PipelineManager:
    def __init__(self, stages):
        self.stages = stages

    def process(self, input_data):
        data = input_data
        for stage in self.stages:
            data = stage.process(data)
        return data

