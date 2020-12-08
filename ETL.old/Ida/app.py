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

@app.route("/quotes")
def quotes():
    result = {}
    result_set = engine.execute('''select id, author_name, text
    from quotes q inner join author a on q.author_name = a.name
    order by id''')
    total_quotes = result_set.rowcount
    quotes = []
    for row in result_set:
        quote = {}
        quote['text'] = row.text
        quote['author'] = row.author_name
        tags = []
        tags_result = engine.execute(
            f'select tag  from tags where quote_id= {row.id}')
        for tagrow in tags_result:
            tags.append(tagrow.tag)
        quote['tags'] = tags
        quotes.append(quote)
    result['quotes'] = quotes
    result['total'] = total_quotes
    return jsonify(result)