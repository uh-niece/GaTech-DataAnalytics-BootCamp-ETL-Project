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

#### Need to uncomment this section once database is setup

# # Create the database instance
# engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()

# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save references to each table
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# # Create our session (link) from Python to the DB
# session = Session(engine)

# Create the flask instance
app = Flask(__name__)

@app.route("/")
def home():
    return ("ETL Project API - Scraping Quotes from the Interwebs<br><br>"
            "Contributors: Anis Ali, Cam Foster, Ida Astaneh, Michael Alread<br><br>"
            "Available API routes are:<br><br>"
            "/quote-api/v1.0/<br>"
            "/quote-api/v1.0/not-landing-page/<br>"
    )

if __name__ == "__main__":
    app.run(debug=True)
