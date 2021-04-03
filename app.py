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

@app.route('/background')
def b_background():
    return render_template('b_background.html')

@app.route('/emissions')
def emissions():
    return render_template('c_emissions.html')

@app.route('/temperatures')
def temperatures():
    return render_template('d_temperatures.html')


@app.route('/clustering')
def clustering():
    return render_template('e_clustering.html')

@app.route('/aboutus')
def aboutus():
    return render_template('f_aboutus.html')
# @app.route('/clustering')
# def clustering():
#     return render_template('e_clustering.html')

# @app.route('/aboutus')
# def aboutus():
#     return render_template('f_aboutus.html')
# @app.route('/kmeans')
# def kmeans():
#     return render_template('kmeans.html')

# @app.route('/the_team')
# def the_team():
#     return render_template('the_team.html')

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/background")
# def background():
#     return render_template("b_background.html")

# @app.route('/emissions')
# def emissions():
#     return render_template('c_emissions.html')

# @app.route('/temperatures')
# def temperatures():
#     return render_template('d_temperatures.html')

# @app.route('/clustering')
# def clustering():
#     return render_template('e_clustering.html')

# @app.route('/aboutus')
# def aboutus():
#     return render_template('f_aboutus.html')


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
