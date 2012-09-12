import os
import gridfs
from django.http import HttpResponse
from pymongo.connection import Connection
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext,loader
from bson.objectid import ObjectId


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


#upload file or health case

def process_health_case(request):
	about = request.POST['about']
	details = request.POST['narrative_text']
	sci_name=request.POST['name']
	connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection = db['healthcase']

	if 'image_scan' in request.FILES.keys():
		image=request.FILES['image_scan']
		fs=gridfs.GridFS(db)
		file_id = fs.put(image,filename="about")
		data={ "about":about, "file_id":file_id , "name" : sci_name }
		collection.insert(data)
	else:
		data={"about":about,"details":details, "name" : sci_name }
		collection.insert(data)		
	return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))
##
#collection = db['controller']
	#data={"a1":about, "b1": details}
	#collection.insert(data)


##	Display image
def my_image(request,image_id):
	connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	fs=gridfs.GridFS(db)
	#image_id="504ba4c9cd274922b1000000"
	image_data = fs.get(ObjectId(image_id))
	return HttpResponse(image_data, mimetype="image/png")

def add_more_reports():
	about = request.POST['about']
	health_case_id=request.POST['health_case_id']
	patient_id=request.POST['patient_id']
	image=request.FILES['image_scan']

	connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection = db['healthreport']
	
	fs=gridfs.GridFS(db)
	file_id = fs.put(image,filename=about)
	data={ "patient_id" : patient_id, "health_case_id":health_case_id, "about":about, "file_id":file_id }
	collection.insert(data)
	return render_to_response('home/new_narrative.html',{ }, context_instance=RequestContext(request))
	
def new_health_report(request):
	return render_to_response('home/new_health_report.html',{ }, context_instance=RequestContext(request))