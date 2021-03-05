import json
import requests
from datetime import datetime, timedelta

def get_data(url):
    date = datetime.now() - timedelta(days = 30)
    date = date.strftime("%Y-%m-%d 23:00:00")

    # Parameters to POST request
    params = {
        'league': 'EPL',
        'season': '2020',
        'n_last_matches': '5',
        'date_start': date
    }

    res = requests.post(url, data = params) # send POST request
    return res.json()  # convert response to json