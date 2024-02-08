from abc import ABC, abstractmethod

class SentimentAnalysisInterface(ABC):
    @abstractmethod
    def analyze_sentiment(message:str)-> str:
        pass
