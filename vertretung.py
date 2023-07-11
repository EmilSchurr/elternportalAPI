#!/usr/bin/python3.7
import requests
from bs4 import BeautifulSoup
from tika import parser
import pandas as pd

pURL = "https://*****.eltern-portal.org/includes/project/auth/login.php"
kURL = "https://*****.eltern-portal.org/login.php"
session = requests.Session()
f = session.get(kURL)

def getCsrf():
  soup = BeautifulSoup(f.text, 'html.parser')
  csrfv = soup.find('input', {'name': 'csrf'})
  strcsrfv = str(csrfv)
  csrfm = strcsrfv[40:]
  csrf = csrfm[:-3]
  return(csrf)

login_data = {
  'csrf': getCsrf(),
	'username': '*****',
	'password': '*****',
	'go_to': ''
	}
f = session.post(pURL, data=login_data)

def getVertretung():
	vertretung = session.get("https://*****.eltern-portal.org/service/vertretungsplan")
	soup = BeautifulSoup(vertretung.text, 'html.parser')
	vg = str(soup.find('div', {'class': 'main_center'}))
	return (vg)
#either use getVertretung() as is or write output to a file as to have it loa faster and not cause more requests to their servers 
#...(handy if you get sql errors in the mornings when everybody tries to log on, but may infringe on DSGVO/GDPR if implemented wrongly)
 g = open('/......./content/v.php','w')
 g.write(getVertretung())
 g.close()
