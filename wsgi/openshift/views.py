import os
from django.http import HttpResponse
from pymongo.connection import Connection
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render_to_response('home/home.html')

def health_record(request):
	t=loader.get_template('home/test.html')
	c=Context({

		})
	return HttpResponse(t.render(c))    

def new_narrative(request):
	 return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))
	 
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


