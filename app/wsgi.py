from flask import Flask, render_template

from .config.config import get_all_config
from .main.payment_methods import get_payment_methods

import app.config.config as conf

app = Flask('adyen-payment-poc')
app.root_path = app.root_path + '/app'
get_all_config()


@app.route('/')
#def home():
 #   return 'Hello World'

@app.route('/')
def home():
    all_payment_methods = get_payment_methods()
    return render_template('dropin.html',payment_methods = all_payment_methods,origin_key = conf.origin_key,method='dropin')
