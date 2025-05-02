import requests
import json

# Định nghĩa URL và headers như yêu cầu
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse: str) -> dict:
    payload = { "raw_document": { "text": text_to_analyse } }
    resp = requests.post(URL, headers=HEADERS, json=payload)
    resp.raise_for_status()
    # Giả sử resp.json() trả về toàn bộ response JSON
    raw = resp.json()['text']      # hoặc key đúng chứa chuỗi JSON cảm xúc
    data = json.loads(raw)        # data là dict ban đầu
    anger    = data['anger']
    disgust  = data['disgust']
    fear     = data['fear']
    joy      = data['joy']
    sadness  = data['sadness']
    scores = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
    dominant = max(scores, key=scores.get)
    # Trả về thuộc tính 'text' của response JSON
    return {**scores, 'dominant_emotion': dominant}


emotion_detector("I am so happy I am doing this.")