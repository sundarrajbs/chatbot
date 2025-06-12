from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI model (requires OPENAI_API_KEY in .env)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Set up conversation memory
memory = ConversationBufferMemory()

# Create the conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # Set to False to disable verbose output
)

def start_chatbot():
    print("Welcome to the LangChain Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = conversation.predict(input=user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    start_chatbot()