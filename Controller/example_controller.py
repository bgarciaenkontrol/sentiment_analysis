
from flask import Blueprint, request, jsonify
from Services.sentiment_analysis_service import SentimentAnalysisService

example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/api/message/ex', methods=['POST'])
def handle_message():
    print('entro')
    data = request.json
    message = data.get('message', '')
    response = analyze(message)
    return jsonify(response)   

def analyze(text):
    sentiment_score = SentimentAnalysisService.analyze_sentiment(text)
    print(sentiment_score + 'ñañaañ')
    return sentiment_score