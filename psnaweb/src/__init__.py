import json

def get_config(key):
    config_file_path = "D://psnaweb//psnaweb//config.json"
    with open(config_file_path, "r") as file:
        config = json.load(file)
    
    if key in config:
        return config[key]
    else:
        raise KeyError("Key '{}' is not found in config.json".format(key))


    #C://Users//swathika//Documents//psnaweb//config.json