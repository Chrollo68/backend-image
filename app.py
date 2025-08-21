from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

# Set API key from Render environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="512x512"
        )
        image_url = response.data[0].url
        return jsonify({"url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "OpenAI Text-to-Image API Backend is running 🚀"
