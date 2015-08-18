import json
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.mail import send_mail
from accounts.forms import RegisterForm
from piebase.models import User

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            username = request.POST.get('username')
            if password == confirm_password:
                json_data = {'error': False}
                new_user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name)
            else:
                json_data = {'error': True, 'error_password': 'password mismatch'}
            return HttpResponse(json.dumps(json_data), content_type = 'application/json')
        else:
            json_data = {'error': True, 'form_errors': register_form.errors}
            return HttpResponse(json.dumps(json_data), content_type = 'application/json')
    return render(request, 'create_account.html')



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username = email, password = password)
        if user:
            if user.is_active:
                auth.login(request, user)
                json_data = {'error': False}
            else:
                json_data = {'error': True, 'error_msg': 'User account is disabled'}
        else:
            json_data = {'error': True, 'error_msg': 'Authenticating user failed, wrong email or password'}
        return HttpResponse(json.dumps(json_data), content_type = 'application/json')
    else:
        return render(request, 'login.html')
        
def forgot_password(request):
    if request.method == 'POST':
        email= str(request.POST.get('email'))
        if not email:
            json_data = {'error': True, 'error_msg': 'This field is required'}
        else:
            if User.objects.filter(email = email).exists():
                json_data = {'error': False}
                #send_mail('Subject here', 'Here is the message.', 'dineshmcmf@gmail.com', [email])
            else:
                json_data = {'error': True, 'error_msg': 'email not registered'}
        return HttpResponse(json.dumps(json_data), content_type = 'application/json')

