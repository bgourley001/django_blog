from django.urls import path
from . import views

# url paths for blog pages
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]