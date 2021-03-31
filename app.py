# import numpy as np
# import pandas as pd
# import json
# import datetime
# # from ps_wd import pswd

# import sqlalchemy
# from sqlalchemy import create_engine, func

from flask import Flask, render_template, redirect

# pswd = 'postgres'

# engine = create_engine('postgresql://postgres:' +
#                        pswd + '@localhost:5432/one_hot_future_db')
# connection = engine.connect()

# Flask Setup
app = Flask(__name__)

# Flask Routes


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/other_predictions')
def charts():
    return render_template('other_predictions.html')

@app.route('/temperatures')
def temperatures():
    return render_template('temperatures.html')

@app.route('/kmeans')
def kmeans():
    return render_template('kmeans.html')

@app.route('/the_team')
def the_team():
    return render_template('the_team.html')


# @app.route("/data")
# def emissions_data():

#     # Establish connection with the database
#     engine = create_engine('postgresql://postgres:' + pswd + '@localhost:5432/one_hot_future_db')
#     connection = engine.connect()

#     results = pd.read_sql(
#         'SELECT * FROM energy_breakdown_emissions', connection)

#     return jsonify((results).to_dict("record"))

if __name__ == '__main__':
    app.run(debug=True)
