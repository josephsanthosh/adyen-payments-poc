import app.config.config as conf
from time import sleep
import requests

def get_payment_methods():
    url = 'https://checkout-test.adyen.com/v52/paymentMethods'

    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = {}
    request_payload["merchantAccount"] = conf.merchant_account
    request_payload["countryCode"] = 'NL'
    request_payload["shopperLocale"] = 'nl-NL'
    print("/paymentMethods request:\n" + str(request_payload))
    make_request = requests.post(url=url, headers=headers, json=request_payload)
    response_object = make_request.text
    print("/paymentMethods response:\n" + response_object)
    return response_object