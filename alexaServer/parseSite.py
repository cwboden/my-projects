import requests
import sys

loginUrl = "https://trueparts.mycccportal.com/ProcurementSSP/poDashboard.html"
visitUrl = "https://trueparts.mycccportal.com/ProcurementSSP/poDashboard.html"
username = "dboden@cccis.com"
password = "Steam1er"

session = requests.Session()

payload = {
    'USERNAME': username,
    'PASSWORD': password,
    'submit': 'id',
}

print payload

r = session.post(loginUrl, data = payload)
print r.text

r = session.get(visitUrl)
print r.text
