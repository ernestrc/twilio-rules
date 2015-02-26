import os, json

DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(DIR, './config/application.json')

with open(CONFIG_FILE, 'r') as opened:
    CONFIG = json.load(opened)
