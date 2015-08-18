from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from piebase.models import Project, User
from django.contrib.auth.decorators import login_required


def list_of_projects(request):
	template_name = 'list_of_projects.html'
	projects_list=Project.objects.all()
	user_objects=User.objects.all()
	dict_items={'projects_list':projects_list, 'user_objects':user_objects}
	return render(request, template_name, dict_items)
