#  GemStory 💎AI

GemStory AI is a web application that generates creative stories using AI.  
Users can choose a genre, define a main character, and instantly generate a story. They can also continue the story with a single click, allowing ideas to grow naturally.

It is designed to be simple, fast, and beginner-friendly.

---

## How we built it

We built GemStory AI as a full-stack web application:

- **Frontend:**  
  - HTML for structure  
  - CSS for a clean and friendly UI  
  - JavaScript to handle user input and API requests  

- **Backend:**  
  - Python with Flask to create a REST API  
  - Flask-CORS to connect frontend and backend  

- **AI:**  
  - Google Gemini API using the **gemini-2.5-flash** model for fast text generation  

The frontend sends user input to the backend, which builds a prompt and sends it to Gemini. The AI-generated story is then returned and displayed to the user.

---


## What's next for GemStory AI

In the future, we would like to:

- Add user accounts and story saving
- Allow users to export stories as files
- Add more genres and customization options
- Improve prompt control for more creative outputs
- Deploy the app online so anyone can use it

GemStory AI has the potential to grow into a powerful creative assistant for storytellers and developers alike.

---
## 🚀 Getting Started
1. Clone the repository:
    ```bash
    git clone https://github.com/devmar07/MLH-hackforhackers-GemStory-AI.git
    ```

1. Get a Gemini API Key:
    https://aistudio.google.com/app/apikey

1. Paste Key into .env file:
    open the .env file and paste the key after 
    ```bash
    GEMINI_API_KEY=
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python api.py
    ```




