from flask import Flask, jsonify, render_template, request, redirect, session, url_for
import requests,os,json
from app import app, main_engine

@app.route('/')
def index():
    return render_template("index.html", result="", lower="", upper="")

@app.route('/validate_input', methods = ['POST'])
def validate_input():
    result = ""
    lower_bound = request.form['lower_bound']
    upper_bound = request.form['upper_bound']   
    if main_engine.validate_inputs(lower_bound, upper_bound):
        result = main_engine.find_random_number(lower_bound, upper_bound)
    else:
        result = "Please input a smaller number to a larger number"
    return render_template("index.html", result = result, lower=lower_bound, upper=upper_bound)
