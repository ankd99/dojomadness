import time
import random

from flask import Flask
import requests

app = Flask(__name__)

start_time = None
quote = None
URL = "http://dojodevopschallenge.s3-website-eu-west-1.amazonaws.com/fortune_of_the_day.json"


def get_quote():
    data = requests.get(URL).json()
    global quote, start_time
    quote = data[random.randint(0, len(data))]['message']
    start_time = time.time()
    return quote


@app.route('/')
def hello_world():
    if start_time and (time.time() - start_time < 10) and quote:
        return quote
    return get_quote()

if __name__ == '__main__':
    app.run()
