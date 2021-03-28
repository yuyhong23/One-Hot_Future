import numpy as np
import pandas as pd
import json
import datetime
from ps_wd import pswd

import sqlalchemy
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import Flask, render_template

# pswd = 'postgres'

engine = create_engine('postgresql://postgres:' +
                       pswd + '@localhost:5432/_db')
connection = engine.connect()

# Flask Setup
app = Flask(__name__)

# Flask Routes


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/charts')
def charts():
    return render_template('charts.html')






@app.route("/data")
def emissions_data():

    # Establish connection with the database
    engine = create_engine('postgresql://postgres:' + pswd + '@localhost:5432/_db')
    connection = engine.connect()

    original_results = pd.read_sql(
        'SELECT * FROM _table limit 10', connection)

    return jsonify((original_results).to_dict("record"))






if __name__ == '__main__':
    app.run(debug=True)
