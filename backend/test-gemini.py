import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key =os.environ.get("GEMINI_API_KEY", "{GEMINI_API_KEY}")
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)