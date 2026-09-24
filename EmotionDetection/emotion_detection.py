import requests
import json

def emotion_detector(text_to_analyse):
    """
    Function to detect emotions in a text using Watson NLP Emotion Predict service
    and format the output into a dictionary with dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Chuyển đổi text response sang dictionary
    formatted_response = json.loads(response.text)
    
    # Trích xuất các điểm cảm xúc từ phản hồi
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Tìm cảm xúc có điểm số cao nhất
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }