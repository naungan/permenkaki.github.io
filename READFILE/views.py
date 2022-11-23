from html import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
import json
import csv


@view_config(route_name='home', renderer='home.jinja2')
def home(request):
	duar = "have a nice day!"
	print("request firstpage")
	return({'data':duar})

#readjson
@view_config(route_name='readjson', renderer='json.jinja2')
def readjson(request):
	with open('Cars.json', 'r') as myfile:
		data=myfile.read()
		x = json.loads(data)
		print("load json file")
		return({'data': x})

#readcsv
@view_config(route_name='readcsv', renderer='csv.jinja2')
def readcsv(request):
	with open('Cars.csv', 'r') as myfile:
		rows = []
		csvreader = csv.reader(myfile)
		header = next(csvreader)
		for row in csvreader:
			rows.append(row)
		print("load csv")
		return({'data': rows,'headnya':header})

#readxml
@view_config(route_name='readxml', renderer='xml.jinja2')
def readxml(request):
	with open('Cars.xml', 'r') as myfile:
		data=myfile.readlines()
		print("load xml file")
		return({'data': data})