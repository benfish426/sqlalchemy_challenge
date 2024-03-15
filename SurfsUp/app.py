# Import the dependencies.

import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Welcome to the Hawaii Climate Analysis API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    entire_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    old_last_date = dt.date(entire_year.year, entire_year.month, entire_year.day)

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= old_last_date).\
              order_by(Measurement.date).all()
    
    precipitation_dict = dict(results)

    print(f"Results for Precipitation: {precipitation_dict}")
    print("Out of Precipitation section")
    
    return jsonify(precipitation_dict)


@app.route("/api/v1.0/stations")
def stations():
    
    #Start session. Query a list of station data, including the station, name, latitude, longitude and elevation.
    
    session = Session(engine)
    sel = [Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    result = session.query(*sel).all()

    session.close()

    #Create an empty list and dictionary. Add row data to dictionary, then append to the list
    stations = []

    for station, name, latitude, longitude, elevation in result:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = latitude
        station_dict["Longitude"] = longitude
        station_dict["Elevation"] = elevation
        stations.append(station_dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)

    
    
    
    
    
    
    
    return(
    )


# @app.route("/api/v1.0/<start>")
# def something...():
#     return(




#     )

# @app.route("/api/v1.0/<start>/<end>")
# def something...():
#     return(




#     )

if __name__ == "__main__":
    app.run(debug=True)