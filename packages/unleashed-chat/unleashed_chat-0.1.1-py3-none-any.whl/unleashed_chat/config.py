import configparser
    
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

def request_model():
    model = input("Please enter the model you would like to use: ")

    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'Unleashed' not in config:
        config.add_section('Unleashed')

    config.set('Unleashed', 'model', model)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Model saved.")

def get_model():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        return config.get('Unleashed', 'model')
    except:
        return "dolphin-2.2.1-mistral-7b"

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        return config.get('Unleashed', 'api_key')
    except:
        return None