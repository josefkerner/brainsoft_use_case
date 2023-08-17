from abc import ABC, abstractmethod
from typing import List, Dict

class Model(ABC):
    @abstractmethod
    def generate(self, texts: List[str]):
        '''
        Will generate content
        :param text:
        :return:
        '''
        pass