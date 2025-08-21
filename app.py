from flask import Flask, request, jsonify
import openai # type: ignore
import os

app = Flask(__name__)

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
            size="512x512"  # can be 256x256, 512x512, 1024x1024
        )
        image_url = response.data[0].url
        return jsonify({"url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "OpenAI Text-to-Image API Backend is running 🚀"
