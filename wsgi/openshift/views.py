import os
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from pymongo.connection import Connection


def home(request):
    return render_to_response('home/home.html')

def health_record(request):
	t=loader.get_template('home/test.html')
	c=Context({

		})
	return HttpResponse(t.render(c))    

def new_narrative(request):
	t=loader.get_template('home/new_narrative.html')
	c=Context({
			context_instance=RequestContext(request)
		})
	return HttpResponse(t.render(c))    

def health_case(request):
	t=loader.get_template('home/health-issue-details.html')
	c=Context({

		})
	return HttpResponse(t.render(c))

def process_health_case(request):
	about = request.POST['about']
	details = request.POST['narrative_text']
	connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection = db['controller']
	data={"a1":about, "b1": narrative_text }
	collection.insert(data)
	new_narrative(request)


