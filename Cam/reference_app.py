# Import all dependencies

from flask import Flask, jsonify
# Leaving out matplotlib dependencies since we don't need them
# %matplotlib inline
# from matplotlib import style
# style.use('fivethirtyeight')
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Create the database instance
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Create the flask instance
app = Flask(__name__)

@app.route("/")
def home():
    return ("Hawaii Weather Data API<br/><br/>"
            "Available Routes:<br/><br/>"
            "/api/v1.0/precipitation<br/>"
            "/api/v1.0/stations<br/>"
            "/api/v1.0/tobs<br/>"
            "/api/v1.0/start<br/>"
            "/api/v1.0/start/end<br/><br/>"
            "In order to get correct results, 'start' and 'end' should be input in YYYY-MM-DD format."
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    sel = [Measurement.date]
    last_date = session.query(*sel).order_by(Measurement.date.desc()).first()[0]
    last_date_dtObj = dt.datetime.strptime(last_date, '%Y-%m-%d')
    first_date_dtObj = last_date_dtObj - dt.timedelta(days=365)
    first_date = first_date_dtObj.strftime("%Y-%m-%d")
    
    sel = [Measurement.date, Measurement.prcp]
    precipitation_results = session.query(*sel).filter(Measurement.date >= first_date).order_by(Measurement.date).all()
    
    precipitation_dict = {}
    for line in precipitation_results:
        key, value = line[0], line[1]
        precipitation_dict[key] = value
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    station_info = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    
    return jsonify(station_info)

@app.route("/api/v1.0/tobs")
def temp_observations():
    sel = [Measurement.date]
    last_date = session.query(*sel).order_by(Measurement.date.desc()).first()[0]
    last_date_dtObj = dt.datetime.strptime(last_date, '%Y-%m-%d')
    first_date_dtObj = last_date_dtObj - dt.timedelta(days=365)
    first_date = first_date_dtObj.strftime("%Y-%m-%d")
 
    # This pulls all the station names and their associated tobs count, then sorts descending so the top value is the most active station (for the last year)
    tobs_info = session.query(Measurement.station, func.count(Measurement.tobs), Measurement.date).filter(Measurement.date>=first_date).group_by(Measurement.station).order_by(func.count(Measurement.tobs).desc()).all()
    most_active = tobs_info[0][0]

    active_station_info = session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.station==most_active, Measurement.date>=first_date).all()
    
    return jsonify(active_station_info)

@app.route("/api/v1.0/<start>")
def temp_query_start(start):
    try:
        # start_date = dt.datetime.strptime(start,"%Y-%m-%d")
        
        data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>=start).all()
        return_dict = {"Minimum Temperature": data[0][0], "Maximum Temperature": data[0][1], "Average Temperature": data[0][2]}
        return jsonify(return_dict)   
    except:
        print("Incorrect Date Format --- formatting should by YYYY-MM-DD")
        return print("Incorrect Date Format --- formatting should by YYYY-MM-DD")
  

@app.route("/api/v1.0/<start>/<end>")
def temp_query_start_end(start, end):
    try:
        # start_date = dt.datetime.strptime(start,"%Y-%m-%d")
        # end_date = dt.datetime.strptime(start,"%Y-%m-%d")
        
        data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date>=start).filter(Measurement.date<=end).all()
        return_dict = {"Minimum Temperature": data[0][0], "Maximum Temperature": data[0][1], "Average Temperature": data[0][2]}
        return jsonify(return_dict)
    except:
        print("Incorrect Date Format --- formatting should by YYYY-MM-DD")
        return print("Incorrect Date Format --- formatting should by YYYY-MM-DD")


if __name__ == "__main__":
    app.run(debug=True)
