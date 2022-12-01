from app.configs.constants import CONFIG
import ndjson

class Data:
    def __init__(self):
        self.path = CONFIG["DATA_PATH"]

    def load_json(self):
        with open(self.path) as file:
            return ndjson.load(file)