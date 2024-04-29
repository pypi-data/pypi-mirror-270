from unleashed_chat.openai_client import get_response
from unleashed_chat.config_handler import get_model
from openai import AuthenticationError

# Runs the chat session.
def run_session(openai_client):
  memory = []
  active_session = True

  print("AI: Hello! How many I assist you today? You can type /help to see available commands.\n")

  while active_session:
    prompt = None
    try:
      prompt = input("You: ")
    except KeyboardInterrupt:
      print("\n\nAI: Goodbye!")
      active_session = False
    try:
      model = get_model()
      response, continue_conversation = get_response(openai_client, prompt, model, memory)
    except AuthenticationError:
      print("\nAI: Invalid API key. Please set your API key using the --set-api-key startup flag and try again.\n")
      return
    if(response != None and response != ""):
      print("\nAI:", response + "\n")
    if(not continue_conversation):
      active_session = False