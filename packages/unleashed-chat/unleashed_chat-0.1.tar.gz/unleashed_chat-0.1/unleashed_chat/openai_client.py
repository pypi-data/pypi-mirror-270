from openai import OpenAI, BadRequestError
from unleashed_chat.config_handler import request_model, get_model

# Creates an OpenAI client with the provided API key
# using the Unleashed.chat API endpoint.
def create_openai_client(api_key):
  return OpenAI(
    base_url='https://unleashed.chat/api/v1',
    api_key=api_key
  )

# Sends a prompt to the OpenAI API and returns the response.
def get_response(openai_client, prompt, model, memory=[]):
  continue_conversation = True
  if(prompt == None):
    return None, continue_conversation
  if(prompt == ""):
    return "Prompt cannot be empty.", continue_conversation
  if(prompt.lower() == "/help"):
    return "Available commands:\n/exit (end the session)\n/reset (reset the memory)\n/models (view available models)\n/model (check the currently used model)\n/setmodel (prompts you to set the model to use)\n/help (view available commands)", continue_conversation
  elif(prompt.lower() == "/exit"):
    continue_conversation = False
    return "Goodbye!", continue_conversation
  elif(prompt.lower() == "/reset"):
    memory.clear()
    return "Memory has been reset! You are now in a new session.", continue_conversation
  elif(prompt.lower() == "/models"):
    response = get_models_list(openai_client)
    return response, continue_conversation
  elif(prompt.lower() == "/setmodel"):
    print("\n" + get_models_list(openai_client) + "\n")
    request_model()
    return "Model has been set!", continue_conversation
  elif(prompt.lower() == "/model"):
    model = get_model()
    return "You are using model: " + model, continue_conversation
  
  memory.append({"role": "user", "content": prompt})

  response_stream = None
  try:
    response_stream = openai_client.chat.completions.create(
      messages=memory,
      model=model,
      stream=True,
    )
  except BadRequestError as e:
    print(f"An error occurred: {e}")
    return str(e), continue_conversation

  response = ""
  for chunk in response_stream:
    response += chunk.choices[0].delta.content

  memory.append({"role": "assistant", "content": response})
  
  return response, continue_conversation

# Return a string with the list of available models.
def get_models_list(openai_client):
  response = "Available models:\n"
  response += "\n".join(model.id for model in openai_client.models.list())
  return response