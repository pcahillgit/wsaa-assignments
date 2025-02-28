# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO and stores it into a file called "cso.json".
# Author: Paul Cahill

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)

# References:
# W3 Schools guide to the requests module: https://www.w3schools.com/python/module_requests.asp
# CSO Data: https://data.cso.ie/
# CSO PxStat information: https://github.com/CSOIreland/PxStat/wiki/API-cube-RESTful