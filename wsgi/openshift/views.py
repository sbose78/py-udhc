import os
import gridfs
from django.http import HttpResponse
from pymongo.connection import Connection
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext,loader


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

	if 'image_scan' in request.FILES.keys():
		image=request.FILES['image_scan']
		fs=gridfs.GridFS(db)
		file_id = fs.put(image,filename="image_scan2")
		data={ "about":about, "file_id":file_id}
		collection.insert(data)
	else:
		data={"about":about,"details":details}
		collection.insert(data)		
	return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))
##
#collection = db['controller']
	#data={"a1":about, "b1": details}
	#collection.insert(data)
##		
	
