import app.config.config as conf
import requests

def get_payment_methods():
    url = 'https://checkout-test.adyen.com/v52/paymentMethods'

    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = {}
    request_payload["merchantAccount"] = conf.merchant_account
    request_payload["countryCode"] = 'NL' #hardcoded to retrieve only payment methods from Netherlands
    request_payload["shopperLocale"] = 'nl-NL'
    
    response_object = requests.post(url=url, headers=headers, json=request_payload)

    return response_object.text