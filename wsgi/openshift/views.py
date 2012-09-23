import os
import gridfs
from django.http import HttpResponse
from pymongo.connection import Connection
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, RequestContext,loader
from bson.objectid import ObjectId

my_sql_connection = Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
my_sql_connection_string='mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE'

def home(request):
    return render_to_response('home/home.html')

def health_record(request):
	t=loader.get_template('home/test.html')
	care_seeker_name=request.GET['name']

	connection=my_sql_connection
	db=connection['BOSE']
	collection=db['healthcase']
	all_narratives=collection.find({
		"name":care_seeker_name
	})

	c=Context({ 
		"narratives_list":all_narratives,
		"patient_name":care_seeker_name
	})
	return HttpResponse(t.render(c))    


# displays form to enter a new narrative

def new_narrative(request):

	connection=Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection=db['scientific_name']


	# change this name later. This returns just one JSON object. Not a collection.
	# scientific_name_list needs to renamed to scientific_name

	scientific_name_list =collection.find_one({
		"status":"unused"
	})

	collection1=db['healthcase']
	returned_names=collection1.group(["name"],None,{'list_a':[]},'function(obj,prev){prev.list_a.push(obj)}')
	unique_names=[]
	for i in range(0,len(returned_names)):
		unique_names.append(returned_names[i]['list_a'][0]['name'])

	dictionary={
		"scientific_name":scientific_name_list,
		"unique_names_list":unique_names
	}


	return render_to_response('home/new_narrative.html',dictionary, context_instance=RequestContext(request))

def fb(request):
	 return render_to_response('home/fb-auth.html',{ }, context_instance=RequestContext(request))

# display details of a specific health case

def health_case(request):

	health_case_id=request.GET['health_case_id']
	connection=Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
	db=connection['BOSE']
	collection=db['healthreport']
	health_reports =collection.find({
		"health_case_id":health_case_id
	})

	collection_healthcase=db['healthcase']
	narrative=collection_healthcase.find({
		"_id":ObjectId(health_case_id)
	})

	t=loader.get_template('home/health-issue-details.html')
	c=Context({

		"narrative":narrative,
		"health_reports":health_reports

		})
	return HttpResponse(t.render(c))


#upload file or health case narrative

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

def add_more_reports(request):
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
	return render_to_response('home/new_health_report.html',{}, context_instance=RequestContext(request))
