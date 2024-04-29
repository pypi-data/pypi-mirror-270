import argparse

def parse_arguments():
  parser = argparse.ArgumentParser(
    prog="Unleashed Chat CLI",
    description='Unleashed Chat CLI',
    epilog="A CLI wrapper for Unleashed.chat's chatbot service."
  )
  parser.add_argument('--set-api-key', action='store_true', help='set your Unleashed API key')
  parser.add_argument('--set-model', action='store_true', help='set the model to use')
  return parser.parse_args()