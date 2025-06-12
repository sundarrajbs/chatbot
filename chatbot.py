from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get model from environment variable or default to gpt-3.5-turbo
model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Initialize the OpenAI model (requires OPENAI_API_KEY in .env)
llm = ChatOpenAI(model=model_name, temperature=0.7)

# Define the prompt template with message history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chatbot assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Create the runnable chain
chain = prompt | llm

# In-memory history store (use a persistent store like SQLite for production)
history_store = {}

def get_session_history(session_id: str):
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]

# Create the chain with message history
conversation = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def start_chatbot():
    print(f"Welcome to the LangChain Chatbot with OpenAI ({model_name})! Type 'exit' to quit.")
    session_id = "default_session"  # Use a unique session ID per user in production
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        # Invoke the chain with the input and session ID
        response = conversation.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        print(f"Bot: {response.content}")

if __name__ == "__main__":
    start_chatbot()