from abc import ABCMeta
from abc import abstractmethod


class Step(ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def process(self,inputs):
        pass


class StepException(Exception):
    pass