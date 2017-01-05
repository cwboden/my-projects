from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

loginUrl = "https://login.trueparts.mycccportal.com/"
visitUrl = "https://trueparts.mycccportal.com/ProcurementSSP/poDashboard.html"
username = "dboden@cccis.com"
password = "Steam1er"

def main():
    session = requests.Session()

    payload = {
    'USERNAME': username,
    'PASSWORD': password,
    'submit': 'id',
    }

    print payload

    r = session.post(loginUrl, data = payload)
    r = session.get(visitUrl)

    web = QWebView()
    web.load(QUrl(visitUrl))
    web.show()

if __name__ == '__main__':
    main()
