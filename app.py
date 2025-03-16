from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Replace with your actual Figma API key
FIGMA_ACCESS_TOKEN = ""
FIGMA_FILE_ID = ""
FIGMA_API_URL = f"https://api.figma.com/v1/files/{FIGMA_FILE_ID}"

@app.route('/fetch-figma-data', methods=['GET'])
def fetch_figma_data():
    headers = {
        "X-Figma-Token": FIGMA_ACCESS_TOKEN
    }
    response = requests.get(FIGMA_API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jsonify({"status": "success", "data": data})
    else:
        return jsonify({"status": "error", "message": "Failed to fetch data from Figma"}), 500

if __name__ == '__main__':
    app.run(debug=True)
