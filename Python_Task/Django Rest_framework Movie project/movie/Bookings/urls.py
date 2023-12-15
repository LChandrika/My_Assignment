from django.urls import path
from . import views

urlpatterns = [
    path('movies',views.Movie_data),
    path('movies/<int:id>',views.Movie_details),
]