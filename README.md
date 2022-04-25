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
	




