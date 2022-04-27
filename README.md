# Web blog project using Django

This project creates a sample web blog using the Django framework.
It is based upon Corey Schafer's Django YouTube Series.

## Blog Django App
Default app created using python manage.py startapp blog

### application url paths
 	- 	Project url paths map application paths to the appropriate application urls.py file
 	-	The application url patterns map the paths to the appropriate page
	-	Application pages are rendered via functions in the application views.py file

### url pattern workflow
	-	project url pattern -> project urls.py -> application urls.py
	-	application url pattern -> application urls.py -> application views.py
	-	application page rendered -> application views.py

### application templates containing page content
	- replace hard-coded html in the views file with html templates from the application templates directory
	- create an html template file for each separate page
	- create a base.html file to contain html which all template html files share
	- a list containing temporary posts was created in views.py to test the logic and styling

### CSS stylesheets
	- place static stylesheets in a static application folder
	- this Web project also uses bootstrap 4 styling
	- bootstrap code was copied from the bootstrap starter template

### Link references
	- replace any hard-coded link references with urlpatterns contained in the application urls.py file
	- this allows application link path references to be placed controlled by a single url pattern
	- this avoids having to change link references in multiple places

### Adding Admin
	- prepare and create admin tables
		- python manage.py makemigrations
		- python manage.py migrate
	- created admin superuser billg using powershell (not git bash)
	- admin access is available via login at localhost:8000/admin/

### Databases, Migrations and add posts interactively
	- Added Post database table via the orm model in models.py
	- Migrate applied to add the table to the database
	- Add posts to the database interactively using python manage.py shell
	- import Post and User objects
		from blog.models import Post
		from django.contrib.auth.models import User
	- Query User objects
		User.objects.all()
	- add a post and save it to the database
		post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
		post_1.save()
	- examine the post
		post = Post.objects.first()
		post.content ... 'First Post Content!'
		post.date_posted ... datetime.datetime(2022, 4, 26, 10, 9, 4, 847204, tzinfo=datetime.timezone.utc)
	- User object is contained in the post so user info can be retrieved directly via the post
		post.author.email ... 'bgourley001@gmail.com'
	- get all posts written by a particular user
		user.post_set.all() ... <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
	- create post for a user using that user's existing post_set, no need to specify author or specify save
		user.post_set.create(title='Blog 3', content='Third Post Content!') ... <Post: Blog 3>
	- replace dummy posts with posts from the database in the views.py file

		from .models import posts

		# Function to handle home page rendering
		def home(request):
		context = {
			'posts': Post.objects.all()
		}

	- format dates in templates (from django date documentation)
		post.date_posted|date:"F d, Y"

	- Register Posts with admin (in admin.py)

		from .models import Post

		admin.site.register(Post)

### User Registration
	- create a separate app for user registration and login.
		python manage.py startapp users
	- add app to settings as an installed app
	- add view to users view.py using django UserCreationForm

		from django.contrib.auth.forms import UserCreationForm

		def register(request):
			# form for a new user
			form = UserCreationForm()
			return render(request, 'users/register.html', {'form': form})

	- add register.html as a user template (extend blog/base.html)


	- create a forms.py file in users to contain our modified forms
	- create UserRegisterForm which extends UserCreationForm to add eg. email field
	- install django-crispy-forms to add extra styling and provide visual error feedback
	- add crispy_forms to INSTALLED APPS and set CRISPY_TEMPLATE_PACK = 'bootstrap4'
	- in register.html modify form printout to be {{ form|crispy }}

### User Login and Logout
	- use django default login view as a starting point
	- import into project urls.py
	- modify users views.py to redirect to the login page upon successful registration
	- create login and logout html templates
	- add conditional in the base template navbar to display login or logout display dependent upon login state	
	- add url route and html template for user's profile
	- add login_required decorator to the profile view to enforce user login upon access attempt to the profile page

### Add Profile Picture
	- To add fields to the existing user model, extend the model in users/models.py
	- import the user model
	- create a Profile class and add required field(s)

		class Profile(models.Model):
			user = models.OneToOneField(User, on_delete=models.CASCADE)
			image = models.ImageField(default='default.jpg', upload_to='profile_pics')

		def __str__(self):
			return f'{self.user.username} Profile'

	- run makemigrations and migrate to apply changes to the database
	- in users/admin.py register the new Profile class with admin

		from .models import Profile

		admin.site.register(Profile)

	- set MEDIA_ROOT and MEDIA_URL in settings.py to set the filesystem location where uploaded media files will be stored and set a URL to that location.

		MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
		MEDIA_URL = '/media/'

	- add html to profile.html to display profile image and info

		<div class="content-section">
      		<div class="media">
        		<img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        	<div class="media-body">
          		<h2 class="account-heading">{{ user.username }}</h2>
          		<p class="text-secondary">{{ user.email }}</p>
        	</div>
      	</div>
      		<!-- FORM HERE -->
    	</div>

    - add media url to project urls

    	from django.conf import settings
		from django.conf.urls.static import static

		...

		if settings.DEBUG:
    		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    - create a signals.py file at project level to handle django signals
    - add create_profile and save_profile functions in signals.py to create a profile when a new user is created, and save the profile when the user object is saved.

    	from django.db.models.signals import post_save
		from django.contrib.auth.models import User
		from django.dispatch import receiver
		from .models import Profile

		# create profile when new user is created
		@receiver(post_save, sender=User)
		def create_profile(sender, instance, created, **kwargs):
			if created:
				Profile.objects.create(user=instance)

		# save profile when user object is saved
		@receiver(post_save, sender=User)
		def save_profile(sender, instance, **kwargs):
			instance.profile.save()

	- import users.signals within the users apps.py file

### Update User Profile
	- update users/forms.py with UpdateUserForm and UpdateProfileForm
	- modify profile.html to display both forms on the same form
	- override save_model to resize image when uploading using Pillow
	- added profile image to user posts on home page

### List, Create, Update, Delete Posts
	- Use django class views to implement List, Create, Update and Delete posts
	- replace function views with class view implementations in the post templates
	








	






