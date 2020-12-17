import requests
import json
import pandas as pd

method =['newCasesPeak', 'deathsPeak','recoveredPeak','status']

def main():
    query = input()
    localurl = query[0:20]
    address = query[20:len(query)]
    newAddress = address.split("?")


    if(localurl=="curl localhost:8080/"):
        if(newAddress[0] ==method[3]):  #if url is right and user wants status
             print("{'status': 'success'}")

        # the url is right and the user want something else then 'status'-now check the end of the request
        else:
            if(len(newAddress)==1): #check if input is only one word
                print("{}")
            else:
                country = newAddress[1][8:len(newAddress[1])]
                url = "https://disease.sh/v3/covid-19/historical/" + country + "?lastdays=30"
                x = requests.get(url)
                status = x.status_code  # to check api success
                y = x.json()

            # newCases
                if (newAddress[0] == method[0] and status == 200):
                    df = pd.DataFrame(y['timeline'])
                    casesPeakDate = df.cases.idxmax()
                    casesPeakValue = df.cases.max()
                    print("{'country':" + country + ",'method':newCasesPeak,'date':" + casesPeakDate, end='')
                    print(" ,'value':", end='')
                    print(casesPeakValue, end='')
                    print("}")

                # deathCase
                elif(newAddress[0] == method[1] and status == 200):
                    df = pd.DataFrame(y['timeline'])
                    deathsPeakDate = df.deaths.idxmax()
                    deathsPeakValue = df.deaths.max()
                    print("{'country':" + country + ",'method':deathsPeak,'date':" + deathsPeakDate, end='')
                    print(" ,'value':", end='')
                    print(deathsPeakValue, end='')
                    print("}")

                # recoveredCase
                elif (newAddress[0] == method[2] and status == 200):
                    df = pd.DataFrame(y['timeline'])
                    recoveredPeakDate = df.recovered.idxmax()
                    recoveredPeakValue = df.recovered.max()
                    print("{'country':" + country + ",'method':deathsPeak,'date':" + recoveredPeakDate, end='')
                    print(" ,'value':", end='')
                    print(recoveredPeakValue, end='')
                    print("}")

                else:  #if the user enter something else
                    print("{}")

    #localurl!="curl localhost:8080/"
    else:
        if(newAddress[0] == method[3]):  #usere wants status
            print("{'status': 'failed'}")
        else: #user wants another parameter
            print("{}")


if __name__ == '__main__':
    main()





