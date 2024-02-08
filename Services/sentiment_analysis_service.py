from pysentimiento import create_analyzer 
analyzer = create_analyzer(task="sentiment", lang="es")
from Interfaces.sentiment_analysis_interface import SentimentAnalysisInterface

class SentimentAnalysisService(SentimentAnalysisInterface):
    @staticmethod
    def analyze_sentiment(message):
        sentiment_score = analyzer.predict(message)


        if sentiment_score.probas['NEG'] > sentiment_score.probas['NEU'] and sentiment_score.probas['NEG'] > sentiment_score.probas['POS']:
            return 'NEG'
        elif sentiment_score.probas['NEU'] > sentiment_score.probas['NEG'] and sentiment_score.probas['NEU'] > sentiment_score.probas['POS']:
            return 'NEU'
        elif sentiment_score.probas['POS'] > sentiment_score.probas['NEG'] and sentiment_score.probas['POS'] > sentiment_score.probas['NEU']:
            return 'POS'
        else:
            return 'ERR'




