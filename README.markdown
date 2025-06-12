# LangChain Chatbot with Grok

   A simple chatbot built with LangChain and xAI's Grok model, featuring conversation memory.

   ## Setup

   1. **Clone the repository**:
      ```bash
      git clone <your-repo-url>
      cd <your-repo-name>
      ```

   2. **Install dependencies**:
      ```bash
      pip install -r requirements.txt
      ```

   3. **Set up environment variables**:
      - Copy `.env.example` to `.env`:
        ```bash
        cp .env.example .env
        ```
      - Add your xAI API key to `.env`:
        ```
        XAI_API_KEY=your_xai_api_key_here
        ```

   4. **Run the chatbot**:
      ```bash
      python chatbot.py
      ```

   ## Usage
   - Type your message and press Enter.
   - Type `exit` to quit the chatbot.
   - The chatbot maintains conversation context using LangChain's memory feature.

   ## Notes
   - Requires an xAI API key (get one from https://x.ai).
   - Ensure Python 3.8+ is installed.