import requests
import random

requests.post("http://127.0.0.1:8000/end", json={"x": random.randint(1, 100), "y": random.randint(1, 100)})
