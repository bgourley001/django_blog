from django.shortcuts import render
from django.http import HttpResponse

# Function to handle home page rendering
def home(request):
	return HttpResponse('<h1>Blog Home</h1>')

#Function to handle about page rendering
def about(request):
	return HttpResponse('<h1>Blog About</h1>')

