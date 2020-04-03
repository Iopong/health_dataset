import time
from db import DBM
from flask import Flask
from requests.exceptions import ConnectionError, Timeout

app = Flask(__name__)

def main():
    try:
        pass
    except ConnectionError:
        print('I cannot connect...')
    except Timeout:
        print('Im timed out...')
    time.sleep(60)

if __name__ = "__main__":
    #do something
    #app.run(port=3000)
