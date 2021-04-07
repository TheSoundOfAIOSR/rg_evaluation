import json


def load_json(file_name):
    """ Load the JSON from a file """
    try:
        with open(file_name) as json_data_file:
            json_data = json.load(json_data_file)
    except FileNotFoundError:
        print(f"Could not open {file_name}")
        raise FileNotFoundError
    print(f"Data successfully loaded from {file_name}.")

    return json_data


def write_to_json(file_name, json_data):
    """ Write JSON data to a file """
    try:
        with open(file_name) as json_data_file:
            json.dump(json_data)
    except FileNotFoundError:
        print(f"Could not open {file_name}")
        raise FileNotFoundError
    print(f"Successfully written {json_data} to {file_name}")
