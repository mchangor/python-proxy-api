from flask import Flask
from RelayServer import relay_get
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
logger = app.logger


@app.route('/', methods=['GET'])
def get_home():
    return "Welcome!"


# Proxy api which forwards all calls to GBIF api via RelayServer
# Variable path stores URI
@app.route('/<path:path>', methods=['GET'])
def get(path):
    logger.info(f"Getting info from path: {path}")
    response = relay_get(path, logger)
    logger.info(f"Received response with code: {response.status_code}")
    return response.content


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=8080)
