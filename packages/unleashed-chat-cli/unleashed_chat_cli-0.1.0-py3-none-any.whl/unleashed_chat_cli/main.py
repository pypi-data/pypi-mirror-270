from openai import OpenAI, AuthenticationError
import argparse
import configparser

active_session = True

def get_response(openai_client, prompt, memory=[]):
  if(prompt.lower() == "/help"):
    return "Available commands:\n/exit (end the session)\n/reset (reset the memory)\n/models (view available models)\n/help (view available commands)"
  elif(prompt.lower() == "/exit"):
    global active_session
    active_session = False
    return "Goodbye!"
  elif(prompt.lower() == "/reset"):
    memory.clear()
    return "Memory has been reset! You are now in a new session."
  elif(prompt.lower() == "/models"):
    response = "Available models:\n"
    response += "\n".join(model.id for model in openai_client.models.list())
    return response
  
  memory.append({"role": "user", "content": prompt})

  response_stream = openai_client.chat.completions.create(
    messages=memory,
    model='dolphin-2.2.1-mistral-7b',
    stream=True,
  )

  response = ""
  for chunk in response_stream:
    response += chunk.choices[0].delta.content

  memory.append({"role": "assistant", "content": response})
  
  return response

def request_api_key():
    api_key = input("Please enter your Unleashed API key: ")

    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'Unleashed' not in config:
        config.add_section('Unleashed')

    config.set('Unleashed', 'api_key', api_key)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("API key saved.")

def main():
  parser = argparse.ArgumentParser(
    prog="Unleashed Chat CLI",
    description='Unleashed Chat CLI',
    epilog="A simple CLI wrapper for Unleashed.chat's chatbot service."
  )
  parser.add_argument('--set-api-key', action='store_true', help='set your Unleashed API key')
  args = parser.parse_args()

  if args.set_api_key:
    request_api_key()
    return
  
  config = configparser.ConfigParser()
  config.read('config.ini')

  api_key = None

  try:
    api_key = config.get('Unleashed', 'api_key')
  except configparser.NoSectionError:
    print("No 'Unleashed' section in the configuration file.")
    return
  except configparser.NoOptionError:
    print("No API key found. Starting setup.")
    request_api_key()
    return

  openai_client = OpenAI(
      base_url='https://unleashed.chat/api/v1',
      api_key=api_key
  )

  memory = []

  print("AI: Hello! How many I assist you today? You can type /help to see available commands.\n")

  while active_session:
    prompt = input("You: ")
    try:
      response = get_response(openai_client, prompt, memory)
    except AuthenticationError:
      print("\nAI: Invalid API key. Please set your API key using the --set-api-key startup flag and try again.\n")
      return
    print("\nAI:", response + "\n")

if __name__ == "__main__":
  main()