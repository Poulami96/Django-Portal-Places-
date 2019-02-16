# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
#from .models import HeadLine, UserProfile

def scrape():
	session=requests.Session()
	session.headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0"}
	url='https://en.wikipedia.org/wiki/Machine_learning#Further_reading'
	content=session.get(url, verify=False).content

	soup=BeautifulSoup(content, "html.parser")
	for link in soup.find_all('span',{'class':'mw-headline'}):
		x=link.text
		print(x)

	for l in soup.find_all('a'):
		if l.has_attr('href'):
			print l.attrs['href']


scrape()
