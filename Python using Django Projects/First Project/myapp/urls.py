from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
]