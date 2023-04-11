from . import views
from django.urls import path

urlpatterns = [
    path("Registration/<str:name>",views.details),
    path("Registration/",views.details),
    
]