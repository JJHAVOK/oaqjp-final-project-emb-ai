"""
This module provides the core logic for the Watson Emotion Detection API.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP API and returns emotion scores.
    
    Args:
        text_to_analyze (str): The text string to analyze.
        
    Returns:
        dict: A dictionary containing scores for emotions and the dominant emotion.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    if not text_to_analyze.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    response = requests.post(url, json=input_json, headers=headers, timeout=5)

    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
    