from django.urls import path
from .views import Employee_details

url_patterns =[
    path("emp/",Employee_details.as_view(),name = 'emp')
]


