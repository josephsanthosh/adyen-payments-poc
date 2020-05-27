from flask import Flask, render_template, request, url_for,redirect

from .config.config import get_all_config
from .main.payment_methods import get_payment_methods
from .main.payment import make_payment
from .main.payment import handle_redirect_shopper
from .main.payment import send_additional_details

import app.config.config as conf

app = Flask('adyen-payment-poc')
app.root_path = app.root_path + '/app'
get_all_config() 


@app.route('/')
#def home():
#   return 'Hello World'

#render landing page
@app.route('/')
def home():
    all_payment_methods = get_payment_methods()
    return render_template('dropin.html',payment_methods = all_payment_methods,origin_key = conf.origin_key)

@app.route('/makePayment', methods=['POST'])
def payment():
    payment_response = make_payment(request)
    return payment_response


@app.route('/additionalDetails', methods=['POST'])
def paymentDetails():
    details_response = send_additional_details(request)
    return details_response


@app.route('/shopperRedirect', methods=['POST', 'GET'])
def handle_redirect():
    values = request.json if request.is_json else request.values.to_dict()  # Get values from request object and convert to python dict
    # Fetch paymentData from the frontend if we have not already
    if 'paymentData' in values:
        response = handle_redirect_shopper(values)
        if response["resultCode"] == 'Authorised':
            print('Authorised\n')
            return redirect(url_for('success'))
        elif response["resultCode"] == 'Received' or response["resultCode"] == 'Pending':
            print('Received\n')
            return redirect(url_for('pending'))
        else:
            print('Failure\n')
            return redirect(url_for('failure'))
    else:
        return render_template('fetchPaymentData.html', values=values)

#render success page
@app.route('/success', methods=['GET'])
def success():
    return render_template('checkout-success.html')

#render failure page
@app.route('/failure', methods=['GET'])
def failure():
    return render_template('checkout-failed.html')

#render success page on pending resulttype
@app.route('/pending', methods=['GET'])
def pending():
    return render_template('checkout-success.html')

#render failure page
@app.route('/error', methods=['GET'])
def error():
    return render_template('checkout-failed.html')