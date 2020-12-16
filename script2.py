import requests

url = 'https://disease.sh/v3/covid-19/historical/Israel?lastdays=30'
myobj = {'12/3/20': '12/9/20'}

x = requests.post(url, data = myobj)

print(x.text)