from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from form import InfoForm

import requests 
import json
import os
import datetime

from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__) 

app.config['SECRET_KEY'] = os.getenv("SECRET")

token = os.getenv("TOKEN")
secret = os.getenv("SECRET")
url = 'https://sandbox.alloy.co/v1/evaluations'


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = InfoForm()

    if form.validate_on_submit():
        # data=jsonify(request.form)
        # data=request.form
        # headers = {'Content-type':'application/json'}
        # response = requests.post(
        #    url, headers=headers, auth= (token, secret), json=data,
        # )

        data = {}
        data['name_first'] = form.name_first.data
        data['name_last'] = form.name_last.data
        data['birth_date'] = form.birth_date.data.strftime('%Y-%m-%d')
        data['document_ssn'] = form.document_ssn.data
        data['email_address'] = form.email_address.data
        data['phone_number'] = form.phone_number.data
        data['address_line_1'] = form.address_line_1.data
        data['address_line_2'] = form.address_line_2.data
        data['address_city'] = form.address_city.data
        data['address_state'] = form.address_state.data
        data['address_postal_code'] = form.address_postal_code.data
        data['address_country_code'] = form.address_country_code.data

        headers = {'Content-type':'application/json'}

        response = requests.post(url, headers=headers, auth = (token, secret), json=data)
        
        response_json = response.json()
        print(response_json["summary"]["result"])

        return response.content
    

    return render_template('apply.html', form=form)
    

if __name__ == '__main__':
    app.run()