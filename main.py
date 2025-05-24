import requests
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_price():
    from_sym = request.args.get("fromSym")
    timestamp_sec = request.args.get("timestampSEC")
    service = request.args.get("service", "coinbase")
    resolution = request.args.get("resolution", "1d")
    to_fiat = request.args.get("toFiat", "USD")
    timezone = request.args.get("timezone", "UTC")

    url = "https://price-svc-utyjy373hq-uc.a.run.app/price"
    params = {
        "fromSym": from_sym,
        "timestampSEC": timestamp_sec,
        "service": service,
        "resolution": resolution,
        "toFiat": to_fiat,
        "timezone": timezone,
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
