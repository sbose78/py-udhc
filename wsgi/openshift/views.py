import os
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from pymongo.connection import connection


def home(request):
    return render_to_response('home/home.html')

def health_record(request):
	t=loader.get_template('home/test.html')
	c=Context({

		})
	return HttpResponse(t.render(c))    

def new_narrative(request):

	connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection = db['controller']
	data={"a1":"b", "b1":"b"}
	collection.insert(data)
	
	t=loader.get_template('home/new_narrative.html')
	c=Context({

		})
	return HttpResponse(t.render(c))    

def health_case(request):
	t=loader.get_template('home/health-issue-details.html')
	c=Context({

		})
	return HttpResponse(t.render(c))

def process_health_case(request):
	about = request.POST['about']
	details = request.POST['details']

