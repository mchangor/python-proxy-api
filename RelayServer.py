# Calls the GBIF api to get information

import requests


def relay_get(uri, logger):
    url = f"https://api.gbif.org/v1/{uri}"
    response = requests.get(url)
    return response
