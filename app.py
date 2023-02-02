#practice
#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
    #return 'Hello world'

#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Flask dependency
from flask import Flask, jsonify


#Access SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflect database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#Create variable for each class to reference 
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create session link
session = Session(engine)

#Define Flask app
app = Flask(__name__)

#Define welcome route
@app.route("/")

#Add routing info for each of the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Create precipitation route
@app.route("/api/v1.0/precipitation")

#Query to get date and precipitation for previous year
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Create stations route
@app.route("/api/v1.0/stations")

#Query to get all the stations
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#Create temperature observations route
@app.route("/api/v1.0/tobs")

#Query primary station for all temp. observations from previous year
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Create stats report route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#Query to select min, avg, & max temps
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)