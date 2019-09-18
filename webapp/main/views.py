from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import NewUserForm
from .utils import generate_random_cookie_pid, call_API
from django.urls import reverse
import requests

# Create your views here.
def homepage(request):
	print("Access home page")
		
	if "cookie_pid" in request.COOKIES.keys():
		cookie_pid = request.COOKIES['cookie_pid']
		print(f"In home page, cookie_pid {cookie_pid} already exists in cookies")
	else:
		cookie_pid = generate_random_cookie_pid()
		print(f"In home page, cookie_pid {cookie_pid} not exist, will add")
		
	
	response = render(request=request, template_name="main/home.html", context={"cookie_pid":cookie_pid})
	response.set_cookie('cookie_pid', cookie_pid)
	return response



def signup(request):
	print("In register")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	print(cookie_pid)

	response = render(request=request, template_name="main/signup.html", context={"cookie_pid":cookie_pid})
	return response

# Create your views here.
def misc1(request):
	print("misc1 page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Car"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)

	response = render(request=request, template_name="main/misc/misc1", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response

# Create your views here.
def misc2(request):
	print("misc2 page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Beauty"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/misc2.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response

# Create your views here.
def car(request):
	print("car page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Car"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/car.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response

# Create your views here.
def beauty(request):
	print("beauty page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Beauty"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/beauty.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	#response.set_cookie(key='cookie_value', value=cookie_value) 
	return response


# Create your views here.
def art(request):
	print("Art page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Art"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/art.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def tech_science(request):
	print("Tech_Science  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Tech_Science"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/tech&science.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def health(request):
	print("Health  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Health"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/health.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def entertainment(request):
	print("entertainment  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Entertainment"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/entertainment.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def business(request):
	print("entertainment  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Entertainment"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)

	response = render(request=request, template_name="main/misc/business.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def sports(request):
	print("Sport  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Sports"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/sports.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response


# Create your views here.
def politics(request):
	print("Politics  page")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	seg_info = "Politics"
	print(f"cookie_pid, {cookie_pid}, seg_info, {seg_info}")

	call_API(seg_info, cookie_pid)
	
	response = render(request=request, template_name="main/misc/politics.html", context={'cookie_pid':cookie_pid, 'seg_info': seg_info})
	return response