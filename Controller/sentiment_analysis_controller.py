from flask import Blueprint, request, jsonify
from Services.sentiment_analysis_service import SentimentAnalysisService

sentiment_analysis_blueprint = Blueprint('sentiment_analysis', __name__)

@sentiment_analysis_blueprint.route('/api/message', methods=['POST'])
def handle_message():
    if request.method == "POST":
        data = request.get_json()
        if 'message' in data:
            message = data['message'] 
            response = analyze(message)
            return jsonify(response) 
        else:
            return jsonify({"error": "No 'message' key found in JSON data"}), 400 
     

def analyze(message):
    return SentimentAnalysisService.analyze_sentiment(message)
     
