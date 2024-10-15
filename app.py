from flask import Flask, request, jsonify
import requests
from getJSON import getJSON

app = Flask(__name__)

# API key and the real API endpoint (replace these with your actual API details)
API_KEY = "762b5d224dmshf42d5d9897e6317p13aa11jsn1b5eb6b7d725"
API_ENDPOINT = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch?location=Los%20Angeles%2C%20CA&status_type=ForSale&home_type=Houses&"
#API_ENDPOINT = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
# The proxy route
@app.route('/proxy', methods=['GET'])
def proxy():
    try:
        # Extract parameters from the incoming request
        params = request.args.to_dict()
        #return params
        # Make the actual request to the external API
        headers = {
            'Authorization': f'Bearer {API_KEY}',  # Or use 'X-API-KEY', etc., depending on the API you're using
            'Content-Type': 'application/json'
        }


        print(params)/prou

        apiHost = "zillow-com1.p.rapidapi.com"

        API_ENDPOINT2 = API_ENDPOINT + "?location=" + params['location']
      
        # Send a request to the external API
        #response = requests.get(API_ENDPOINT, headers=headers, params=params)
        response = getJSON(API_ENDPOINT2,apiHost)

        return response
        # Return the response from the API
        #return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
