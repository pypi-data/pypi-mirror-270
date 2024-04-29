from unleashed_chat.openai_client import create_openai_client
from unleashed_chat.config_handler import request_api_key, request_model, get_api_key
from unleashed_chat.session import run_session
from unleashed_chat.cli import parse_arguments

# Gets config information and start the session.
def main():
  args = parse_arguments()

  if args.set_api_key:
    request_api_key()
    return
  elif args.set_model:
    request_model()
    return
  
  api_key = get_api_key()
  if api_key is None:
      return

  openai_client = create_openai_client(api_key)

  run_session(openai_client)

if __name__ == "__main__":
  main()