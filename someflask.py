from flask import Flask, request, jsonify, make_response
import os
import dialogflow
import requests
import json
import common_utils
import requests

app = Flask(__name__)

@app.route('/')
def index():
    print "hello"
    return '{"name":"Gaurab"}'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    # print req
    # print json.dumps(req)

    # fetch action from json
    # action = req.get('queryResult').get('action')
    intent = req.get('queryResult').get('intent')
    # print intent
    intentName = intent.get('displayName')
    print intentName
    data = {}
    if intentName == 'Alation-down':
        r = requests.get(common_utils.ALATION_HEALTH_URL)
        if r.status_code != 200:
            data["text"]= 'Opps! Alation seems to be down.http returned {} code'.format(r.status_code)
        else:
            json_str = r.json()
            if json_str['alation-api']['status'] == 'ok' and json_str['metadata-api'] == 'ok':
                data['alation_status_text'] = 'Alation is UP and Healthy'
            else:
                data['alation_status_text'] = 'Alation is DOWN'
            data['api_response'] = json_str
    else:
        with open('intent.json', 'r') as f:
            intent_dict = json.load(f)
            intent_data = intent_dict.get(intentName)
            print intent_data
            data['action'] = intent_data.get('response')



    # return a fulfillment response
    # return {'fulfillmentText': 'This is a response from webhook.'}
    return {'fulfillmentText': json.dumps(data, indent=2)}

@app.route('/webhook', methods=['POST'])
def webhook():
    # print 'Hello!'
    return make_response(jsonify(results()))

# run Flask app
if __name__ == "__main__":
    app.run()