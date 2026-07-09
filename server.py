"""
This module defines the Flask web server routes for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from final_project.emotion_detection import emotion_detector

app = Flask("Emotion Detector", template_folder='templates', static_folder='static')

@app.route("/emotionDetector")
def sent_detector():
    """
    Handles the request, calls the detector, and returns the formatted results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5502)
