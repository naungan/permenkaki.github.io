from html import escape
import sqlite3
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.jinja2')
def home(request):
	print("request firstpage")
	cdb = sqlite3.connect('cars.db')
	k = cdb.cursor()
	k.execute(
	    """
	        SELECT * FROM TBCars
	    """
	    )
	data = k.fetchall()
	cdb.commit()
	cdb.close()
	return({'data':data})

@view_config(route_name='create', renderer='home.jinja2')
def create(request):
		cdb = sqlite3.connect('cars.db')
		k = cdb.cursor()
		k.execute(
		    """
		        INSERT INTO TBCars(
			        carID,
			        carbrand,
			        carmodel,
			        carprice
		        )
		        VALUES(
		        	"300",
		        	"Toyota",
		        	"Trueno",
		        	"900"
		        )
		    """
		    )
		data = k.fetchall()
		cdb.commit()
		cdb.close()
		return({'data':"NEW DATA ADDED"})

@view_config(route_name='update', renderer='home.jinja2')
def update(request):
	cdb = sqlite3.connect('cars.db')
	k = cdb.cursor()
	k.execute(
	    """
	        UPDATE TBCars
	        SET carID = "86"
	        WHERE carID = "300"
	    """
	    )
	data = k.fetchall()
	cdb.commit()
	cdb.close()
	return({'data':"DATA UPDATED"})

@view_config(route_name='delete', renderer='home.jinja2')
def delete(request):
	cdb = sqlite3.connect('cars.db')
	k = cdb.cursor()
	k.execute(
	    """
	        DELETE FROM TBCars
	        WHERE carbrand = "Toyota"
	    """
	    )
	data = k.fetchall()
	cdb.commit()
	cdb.close()
	return({'data':"CHOSEN DATA ERASED"})

