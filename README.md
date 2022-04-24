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