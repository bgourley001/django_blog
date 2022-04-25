from django.shortcuts import render

#fake posts
posts = [
	{
		'author': 'beegee',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 24, 2022'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 25, 2022'	
	}
]

# Function to handle home page rendering
def home(request):
	context = {
		'posts': posts
	}

	return render(request, 'blog/home.html', context)

#Function to handle about page rendering
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

