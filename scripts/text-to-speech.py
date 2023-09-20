import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>/stream"  # Replace <voice-id> with the desired voice ID

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "d78d5c1bfd9c571152062225ca297ee9"  
}

data = {
  "text": "सेब एक फल है। सेब का रंग लाल या हरा होता है। वैज्ञानिक भाषा में इसे मेलस डोमेस्टिका (Malus domestica) कहते हैं। इसका मुख्यतः स्थान मध्य एशिया है। इसके अलावा बाद में यह यूरोप में भी उगाया जाने लगा। यह हजारों वर्षों से एशिया और यूरोप में उगाया जाता रहा है। इसे एशिया और यूरोप से उत्तरी अमेरिका बेचा जाता है। इसका ग्रीक, वेनिंज़ूला और यूरोप में धार्मिक महत्व है",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers, stream=True)

with open('output_11.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)