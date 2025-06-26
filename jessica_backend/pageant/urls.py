from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # temporary test view
]

 
urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
]
 
 
urlpatterns = [
    path('', views.gallery, name='gallery'),  # Gallery becomes the home page
    path('home/', views.home, name='home'),   # Optional: keep "Hello" on /home/
]

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('photo/<int:pk>/edit/', views.edit_photo, name='edit_photo'),
    path('photo/<int:pk>/delete/', views.delete_photo, name='delete_photo'),
]

 
