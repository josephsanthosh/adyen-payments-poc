import app.config.config as conf

import requests
from json import loads
import uuid

def make_payment(payment_request):
    url = 'https://checkout-test.adyen.com/v52/payments'
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = payment_request.get_json()
    
    
    request_payload["amount"] = {"currency": 'EUR',"value": "1000"} #hardcoding payment amount to EUR 10
    request_payload["merchantAccount"] = conf.merchant_account
    request_payload["returnUrl"] = conf.server_name + '/shopperRedirect'
    request_payload["reference"] = str(uuid.uuid4()) #auto-generating unique reference number for current context
    request_payload["channel"] = 'Web'


    #setting extra fields in request payload for 3ds2 enabled card payments
    if request_payload["paymentMethod"]["type"] == 'scheme':
        request_payload["additionalData"] = {"allow3DS2": "true"}
        request_payload["origin"] = conf.server_name
        request_payload["shopperIP"] = "127.0.0.1"


        """ 
        Removing fields 'encryptedCardNumber', 'encryptedExpiryMonth', 
        'encryptedExpiryYear', 'encryptedSecurityCode' recieved from front-end 
        and replacing with raw data fields. Reason documented in README.MD
        """
        del request_payload["paymentMethod"]["encryptedCardNumber"]
        del request_payload["paymentMethod"]["encryptedExpiryMonth"]
        del request_payload["paymentMethod"]["encryptedExpiryYear"]
        del request_payload["paymentMethod"]["encryptedSecurityCode"]

        request_payload["paymentMethod"]["expiryMonth"] = '03'
        request_payload["paymentMethod"]["expiryYear"] = '2030'
        request_payload["paymentMethod"]["number"] = '371449635398431'
        request_payload["paymentMethod"]["cvc"] = '7373'


    response_object = requests.post(url=url, headers=headers, json=request_payload)
    return response_object.text

"""
Function to handle onAddtionalDetails request calls
"""
def send_additional_details(details_request):
    url = 'https://checkout-test.adyen.com/v52/payments/details'
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = details_request.get_json() #convert request object to json

    response_object = requests.post(url=url, headers=headers, json=request_payload)
    return response_object.text


"""
Function to handle onAddtionalDetails request calls for shopper redirect operations
"""
def handle_redirect_shopper(values):
    url = 'https://checkout-test.adyen.com/v52/payments/details'
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    response_object = requests.post(url=url, headers=headers, json=values)
    return loads(response_object.text) #convert to python dict for easy parsing. Inspired by Adyen github code