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


@app.route('/newCasesPeak?country=israel') #newCasesPeak
def newCasesPeak():
    url = "https://disease.sh/v3/covid-19/historical/israel?lastdays=30"
    x = requests.get(url)
    y = x.json()
    df = pd.DataFrame(y['timeline'])
    casesPeakDate = df.cases.idxmax()
    casesPeakValue = df.cases.max()
    return '{“country”:”israel”,“method”:“newCasesPeak”,”date”:"' +casesPeakValue +'",“value”:' + newCasesPeak


if __name__ == '__main__':
    app.run(host='0.0.0.0')






    
