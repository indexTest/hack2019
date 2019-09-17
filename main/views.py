from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import NewUserForm

# Create your views here.
def homepage(request):
	return render(request=request, 
				template_name="main/home.html",
				context={"tutorials": Tutorial.objects.all})


def register(request):
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
