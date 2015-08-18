from django.shortcuts import render
from django.http import HttpResponse
from piebase.models import Project
from forms import CreateProjectForm
from django.utils import timezone
from django.template.defaultfilters import slugify
import json
# Create your views here.

def create_project(request):
	template_name = 'create_project.html'
	dictionary = {}
	if(request.method=="POST"):
		# project  = Project.objects.create(name="project1",description="project1")
		
		# print request.POST
		form = CreateProjectForm(request.POST)
		if(form.is_valid()):
			slug = slugify(request.POST['name'])
			# print request.user
			# organization=request.user.organization
			# Project.objects.create(name=request.POST['name'],slug=slug,description=request.POST['description'],modified_date=timezone.now(),organization=organization)
			return HttpResponse(json.dumps({'error':False,'errors':form.errors}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({'error':True,'errors':form.errors}), content_type="application/json")
		#return HttpResponse(request.POST)
	return render(request,template_name,dictionary)
	# return HttpResponse("Hello")