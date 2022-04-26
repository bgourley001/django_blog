from django.shortcuts import render
from .models import Post

# Function to handle home page rendering
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

#Function to handle about page rendering
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

