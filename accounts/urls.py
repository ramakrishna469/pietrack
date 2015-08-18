from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'login/', 'accounts.views.login', name = 'login'),
    url(r'register/', 'accounts.views.register', name = 'register'),
    url(r'forgot_password/', 'accounts.views.forgot_password', name = 'forgot_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
