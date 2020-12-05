########## Flask API for ETL Project ##########
## Cam Foster
## Anis Ali
## Michael Alread
## Ida Astaneh

# Import all dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Create the flask instance
app = Flask(__name__)
app.config["DEBUG"] = True

connection_string = 'postgres://iljeyeekqbmawa:14a1e06b7556d81e7154a5983966a4bf2e2c1139cd0a30beb10a12e17b1868c9@ec2-52-22-238-188.compute-1.amazonaws.com:5432/dd6g3lf7c51860'
engine = create_engine[connection_string]

@app.route('/', methods=['GET'])
def index():
    return templates("index.html", listing = listing)

app.add_url_rule("/quotes","quotes",quotes)