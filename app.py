from flask import Flask, request, jsonify
import openai  # type: ignore
import os

app = Flask(__name__)

# Set API key from Render environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-image", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt")
    size = data.get("size", "1024x1024")  # ✅ default to 1024x1024

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # ✅ Only allow supported sizes
    valid_sizes = ["1024x1024", "1024x1536", "1536x1024", "auto"]
    if size not in valid_sizes:
        size = "1024x1024"

    try:
        response = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size  # ✅ dynamic size
        )
        image_url = response.data[0].url
        return jsonify({"url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "OpenAI Text-to-Image API Backend is running 🚀"

