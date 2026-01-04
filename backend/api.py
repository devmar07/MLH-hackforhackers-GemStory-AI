import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)


api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

@app.route("/story", methods=["POST"])
def story():
    data = request.json
    genre = data.get("genre", "")
    character = data.get("character", "")
    history = data.get("history", "")

    prompt = f"""
You are a creative AI copilot for hackers.

Write a short story.

Genre: {genre}
Main character: {character}

Previous story:
{history}

Continue the story in a creative and concise way.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({
        "story": response.text
    })

if __name__ == "__main__":
    app.run(debug=True)
