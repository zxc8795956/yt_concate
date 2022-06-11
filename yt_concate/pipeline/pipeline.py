from yt_concate.pipeline.Steps.step import StepException


class Pipeline:
    def __ini__(self, steps):
        self.steps = steps

    def run(self):
        for step in self.steps:
            try:
                step.process()
            except StepException as e:
                print('Exception happens', e)
                break

