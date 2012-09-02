import os
from django.shortcuts import render_to_response
from django.template import Context, loader

def home(request):
    return render_to_response('home/home.html')

def narrative(request):
	t=loader.get_template('home/test.html')
	c=Context({

		})
	return HttpResponse(t.render(c))    
