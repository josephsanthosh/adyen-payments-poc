from flask import Flask

from .config.config import get_all_config

app = Flask('adyen-payment-poc')
app.root_path = app.root_path + '/app'
get_all_config()


@app.route('/')
#def home():
 #   return 'Hello World'

