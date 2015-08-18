from django.conf.urls import include, url
import views


urlpatterns = [

	url(r'^list-of-projects/$', views.list_of_projects, name='list_of_projects'),
]
