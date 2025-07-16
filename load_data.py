import json

def load_producthunt_data():
    with open("output.json", "r") as f:
        return json.load(f)
