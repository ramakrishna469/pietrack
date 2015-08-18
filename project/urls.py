from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^create-project/$',views.create_project,name='create_project'),
]