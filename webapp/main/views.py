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



def register(request):
	print("In register")
	cookie_pid = request.COOKIES.get('cookie_pid') 
	print(cookie_pid)

	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			print("valid")
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as : {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages}")

	form = NewUserForm
	return render(request, "main/register.html", context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			print("valid")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			for msg in form.error_messages:
				print(f"username: {username}, password: {password}")
			user = authenticate(username = username, password = password)	
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as : {username}")
				return redirect("main:homepage")
			else:
				for msg in form.error_messages:
					messages.error(request, f"{msg}:{form.error_messages}")
				messages.error(request, f"invalid username or password")
		else:
			messages.error(request, f"invalid username or password")

	form = AuthenticationForm()
	return render(request, "main/login.html", {"form":form})


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
