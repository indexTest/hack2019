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
		
	if "pid" in request.COOKIES.keys():
		pid = request.COOKIES['pid']
		print(f"In home page, pid {pid} already exists in cookies")
	else:
		pid = generate_random_cookie_pid()
		print(f"In home page, pid {pid} not exist, will add")
		
	
	response = render(request=request, template_name="main/home.html", context={"pid":pid})
	response.set_cookie('pid', pid)
	return response



def signup(request):
	print("In register")
	pid = request.COOKIES.get('pid') 
	print(pid)

	response = render(request=request, template_name="main/signup.html", context={"pid":pid})
	return response

# Create your views here.
def misc1(request):
	print("misc1 page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Car"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)

	response = render(request=request, template_name="main/misc/misc1", context={'pid':pid, 'seg_info': seg_info})
	return response

# Create your views here.
def misc2(request):
	print("misc2 page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Beauty"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/misc2.html", context={'pid':pid, 'seg_info': seg_info})
	return response

# Create your views here.
def car(request):
	print("car page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Car"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/car.html", context={'pid':pid, 'seg_info': seg_info})
	return response

# Create your views here.
def beauty(request):
	print("beauty page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Beauty"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/beauty.html", context={'pid':pid, 'seg_info': seg_info})
	#response.set_cookie(key='cookie_value', value=cookie_value) 
	return response


# Create your views here.
def art(request):
	print("Art page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Art"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/art.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def tech(request):
	print("Tech_Science  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Tech_Science"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/tech.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def health(request):
	print("Health  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Health"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/health.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def entertainment(request):
	print("entertainment  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Entertainment"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/entertainment.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def business(request):
	print("entertainment  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Entertainment"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)

	response = render(request=request, template_name="main/misc/business.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def sports(request):
	print("Sport  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Sports"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/sports.html", context={'pid':pid, 'seg_info': seg_info})
	return response


# Create your views here.
def politics(request):
	print("Politics  page")
	pid = request.COOKIES.get('pid') 
	seg_info = "Politics"
	print(f"pid, {pid}, seg_info, {seg_info}")

	call_API(seg_info, pid)
	
	response = render(request=request, template_name="main/misc/politics.html", context={'pid':pid, 'seg_info': seg_info})
	return response