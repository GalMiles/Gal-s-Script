import requests
import json
import pandas as pd

method =['newCasesPeak', 'deathsPeak','recoveredPeak','status']

def main():
    query = input()
    #geting to the method
    address = query[20:len(query)]
    newAddress = address.split("?")
    country = newAddress[1].strip("country=")

    url = "https://disease.sh/v3/covid-19/historical/"+country+"?lastdays=30"
    print(url)
    x =requests.get(url)

    y = x.json()

    #newCases
    if(newAddress[0] == method[0]):
        df = pd.DataFrame(y['timeline'])
        casesPeakDate = df.cases.idxmax()
        casesPeakValue = df.cases.max()
        print("{'country':"+country+",'method':newCasesPeak,'date':"+casesPeakDate, end='')
        print(" ,'value':",end='')
        print(casesPeakValue, end='')
        print("}")

        #deathCase
    elif(newAddress[0] == method[1]):
        df = pd.DataFrame(y['timeline'])
        deathsPeakDate = df.deaths.idxmax()
        deathsPeakValue = df.deaths.max()
        print("{'country':"+country+",'method':deathsPeak,'date':"+deathsPeakDate, end='')
        print(" ,'value':",end='')
        print(deathsPeakValue, end='')
        print("}")


    recoverPeak = df.recovered.max()
    #print(df.cases.idxmax())

if __name__ == '__main__':
    main()





