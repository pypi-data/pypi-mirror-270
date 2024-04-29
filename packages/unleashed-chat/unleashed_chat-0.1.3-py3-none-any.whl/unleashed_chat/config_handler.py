import configparser

# Gets the configuration file.
def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Unleashed' not in config:
        config.add_section('Unleashed')
    return config

# Requests the user to input their Unleashed API key.
def request_api_key():
    api_key = input("Please enter your Unleashed API key: ")

    config = get_config()

    if 'Unleashed' not in config:
        config.add_section('Unleashed')

    config.set('Unleashed', 'api_key', api_key)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("API key saved.")

# Requests the user to input the model they would like to use.
def request_model():
    model = input("Please enter the model you would like to use: ")

    config = get_config()

    if 'Unleashed' not in config:
        config.add_section('Unleashed')

    config.set('Unleashed', 'model', model)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("Model saved.")

# Gets the model from the configuration file.
def get_model():
    config = get_config()
    model = None
    try:
        model = config.get('Unleashed', 'model')
    except:
        model = "dolphin-2.2.1-mistral-7b"
    return model

# Gets the API key from the configuration file.
def get_api_key():
    config = get_config()
    try:
        return config.get('Unleashed', 'api_key')
    except configparser.NoSectionError:
        print("No 'Unleashed' section in the configuration file.")
    except configparser.NoOptionError:
        print("No API key found. Starting setup.")