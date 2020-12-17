import requests
import json
import pandas as pd
from flask import Flask, redirect, url_for, request
method =['newCasesPeak', 'deathsPeak','recoveredPeak','status']
countries =['israel', 'england']

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/') #empty
def empty():
    return '{}'

@app.route('/status') #status
def status():
     return '{“status”: “success”}'



if __name__ == '__main__':
    app.run(host='0.0.0.0')






    
