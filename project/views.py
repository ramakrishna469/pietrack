from django.shortcuts import render
from django.http import HttpResponse
from piebase.models import Project,Organization
from forms import CreateProjectForm
from django.utils import timezone
from django.template.defaultfilters import slugify
import json
# Create your views here.

def create_project(request):
	template_name = 'create_project.html'
	dictionary = {}
	if(request.method=="POST"):		
		organization=Organization.objects.all()[0]#request.user.organization
		# print "before form"
		form = CreateProjectForm(request.POST,organization=organization)
		# print "after form"
		if(form.is_valid()):
			slug = slugify(request.POST['name'])
			# Project.objects.create(name=request.POST['name'],slug=slug,description=request.POST['description'],modified_date=timezone.now(),organization=organization)
			return HttpResponse(json.dumps({'error':False,'errors':form.errors}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({'error':True,'errors':form.errors}), content_type="application/json")
	return render(request,template_name,dictionary)
