import requests
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

# Simpan file CSV dari URL
@app.route('/api/v1/generate', methods=['POST'])
def generate_csv():
    url = "https://github.com/paldapd/Python-API/raw/main/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        return Response(content, content_type='text/csv; charset=utf-8')
    else:
        return "Failed to download the CSV", 500

# Layani file CSV sebagai octet-stream
@app.route('/api/v1/download', methods=['GET'])
def download_csv():
    url = "https://github.com/paldapd/Python-API/raw/main/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content
        return Response(content, content_type='application/octet-stream')
    else:
        return "Failed to download the CSV", 500

# Contoh fungsi untuk mengirim data ke message queue
def send_to_message_queue(data):
    # Implementasi pengiriman data ke message queue di sini
    pass

# Mengirim data ke message queue
@app.route('/api/v1/send_mq', methods=['GET'])
def send_data_to_mq():
    data = {"message": "Hello, Message Queue!"}
    send_to_message_queue(data)
    return "Data sent to message queue"

if __name__ == '__main__':
    app.run(debug=True)
