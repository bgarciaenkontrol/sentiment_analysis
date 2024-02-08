from flask import Flask
from Controller.sentiment_analysis_controller import sentiment_analysis_blueprint
from Controller.example_controller import example_blueprint

app = Flask(__name__)
app.register_blueprint(sentiment_analysis_blueprint)
app.register_blueprint(example_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

