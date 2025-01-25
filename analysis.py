import os
import requests
import base64
from io import BytesIO
from openai import OpenAI

client = OpenAI()

def download_image(image_url):
    response = requests.get(image_url)
    return BytesIO(response.content)

def encode_image(image_data):
    return base64.b64encode(image_data.getvalue()).decode('utf-8')

def analyze_cartoon(cartoon_url):
    try:
        image_data = download_image(cartoon_url)
        base64_image = encode_image(image_data)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Provide a short and concise analysis to this political cartoon."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ]
                }
            ]
        )
        return response.choices[0].message.content
        #print(response)
    except Exception as e:
        return e