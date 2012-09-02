import os
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse

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

		})
	return HttpResponse(t.render(c))    

def health_case(request):
	t=loader.get_template('home/health-issue-details.html')
	c=Context({

		})
	return HttpResponse(t.render(c))




