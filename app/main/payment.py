import app.config.config as conf
import requests
from random import randint
from json import loads
import uuid

def make_payment(payment_request):
    url = 'https://checkout-test.adyen.com/v52/payments'
    print('\nADDITIONAL DATA REQUEST\n')
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = payment_request.get_json()
    
    request_payload["amount"] = {"currency": 'EUR',"value": "1000"}
    request_payload["merchantAccount"] = conf.merchant_account
    request_payload["returnUrl"] = conf.server_name + '/shopperRedirect'
    request_payload["reference"] = str(uuid.uuid4())
    request_payload["channel"] = 'Web'

    if request_payload["paymentMethod"]["type"] == 'scheme':
        request_payload["additionalData"] = {"allow3DS2": "true"}
        request_payload["origin"] = conf.server_name
        request_payload["shopperIP"] = "127.0.0.1"

        del request_payload["paymentMethod"]["encryptedCardNumber"]
        del request_payload["paymentMethod"]["encryptedExpiryMonth"]
        del request_payload["paymentMethod"]["encryptedExpiryYear"]
        del request_payload["paymentMethod"]["encryptedSecurityCode"]

        request_payload["paymentMethod"]["expiryMonth"] = '03'
        request_payload["paymentMethod"]["expiryYear"] = '2030'
        request_payload["paymentMethod"]["number"] = '371449635398431'
        request_payload["paymentMethod"]["cvc"] = '7373'





    print("/payments request:\n" + str(request_payload))
    make_request = requests.post(url=url, headers=headers, json=request_payload)
    response_object = make_request.text
    print("/payments response:\n" + response_object)

    return response_object


def send_additional_details(details_request):
    url = 'https://checkout-test.adyen.com/v52/payments/details'
    print("\ADDITIONAL DETAILS TRIGGERED\n")
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    request_payload = details_request.get_json()

    print("/payments/details request:\n" + str(request_payload))
    r = requests.post(url=url, headers=headers, json=request_payload)
    response = r.text
    print("payments/details response:\n" + response)
    return response

def handle_redirect_shopper(values):
    url = 'https://checkout-test.adyen.com/v52/payments/details'
    print("\nSHOPPER REDIRECT\n")
    headers = {"Content-type": "application/json","X-Api-Key": conf.api_key}

    print("/payments/details request:\n" + str(values))
    r = requests.post(url=url, headers=headers, json=values)
    print("/payments/details response:\n" + r.text)
    print('LOADS',loads(r.text))
    return loads(r.text)