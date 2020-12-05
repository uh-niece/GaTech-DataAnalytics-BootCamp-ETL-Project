########## Flask API for ETL Project ##########
## Cam Foster
## Anis Ali
## Michael Alread
## Ida Astaneh

# Import all dependencies

from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

app = Flask(__name__)
connection_string = 'postgres://iljeyeekqbmawa:14a1e06b7556d81e7154a5983966a4bf2e2c1139cd0a30beb10a12e17b1868c9@ec2-52-22-238-188.compute-1.amazonaws.com:5432/dd6g3lf7c51860'
engine = create_engine(connection_string)

@app.route("/")
def home():
    return ("ETL Project API - Scraping Quotes from the Interwebs<br><br>"
            "Contributors: Anis Ali, Cam Foster, Ida Astaneh, Michael Alread<br><br>"
            "Available API routes are:<br><br>"
            "/quote-api/quotes<br>"
            "/quote-api/authors<br>"            
            "/quote-api/top10tags<br>"
    )

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

@app.route("/authors")
def authors():
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

@app.route("/top10tags")
def top10tags():
    result = []
    result_set = engine.execute('''select tag, count(*) as total from tags where tag<>'attributed-no-source' group by tag order by total desc, tag desc limit 20''')
    for row in result_set:
        tag = {"tag":row.tag, "total":row.total}
        result.append(tag)
    return jsonify(result)

# @app.route("/authors/authornames")
# def authornames():
#     return("In work.")

# @app.route("/quote-api/v1.0/tags")
# def tags():
#     return("In work.")

# @app.route("/quote-api/v1.0/tags/<tag>")
# def tags_search(tag):
#     return("In work.")

if __name__ == "__main__":
    app.run(debug=True)
