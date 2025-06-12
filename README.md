LangChain Chatbot
A simple chatbot built with LangChain and OpenAI's GPT-3.5-turbo model, featuring conversation memory.
Setup

Clone the repository:
git clone <your-repo-url>
cd <your-repo-name>


Install dependencies:
pip install -r requirements.txt


Set up environment variables:

Copy .env.example to .env:cp .env.example .env


Add your OpenAI API key to .env:OPENAI_API_KEY=your_openai_api_key_here




Run the chatbot:
python chatbot.py



Usage

Type your message and press Enter.
Type exit to quit the chatbot.
The chatbot maintains conversation context using LangChain's memory feature.

Notes

Requires an OpenAI API key (get one from https://platform.openai.com).
Ensure Python 3.8+ is installed.

