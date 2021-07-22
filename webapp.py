from flask import Flask, redirect, Markup, url_for, session, request, jsonify
from flask import render_template

import pprint
import os
import sys
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

app = Flask(__name__)

try:
    credentials = {
        "type": "service_account",
        "project_id": os.environ['project_id'],
        "private_key_id": os.environ['private_key_id'],
        "private_key": os.environ['private_key'].replace('\\n', '\n'),
        "client_email": os.environ['client_email'],
        "client_id": os.environ['client_id'],
        "auth_uri": os.environ['auth_uri'],
        "token_uri": os.environ['token_uri'],
        "auth_provider_x509_cert_url": os.environ['auth_provider_x509_cert_url'],
        "client_x509_cert_url": os.environ['client_x509_cert_url']
    }
    gp = gspread.service_account_from_dict(credentials)
    gsheet = gp.open('Copy of Watershed Brigade')
    wsheet = gsheet.worksheet('2021 Wba Tracking')
except:
    sys.exit("Unable to Render Resource")

@app.route('/') #change start route later?
def render_map():
    return render_template('map.html', data = wsheet.get_all_values())
