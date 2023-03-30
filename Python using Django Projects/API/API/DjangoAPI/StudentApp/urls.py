from django.urls import path
from StudentApp import views

urlpatterns = [
    path('student/', views.studentApi),
    path('student/<int:id>',views.studentApi),
    path('purchase/', views.purchaseApi),
    path('purchase/<int:id>',views.purchaseApi),
    path('email/', views.emailApi),
    path('sms/', views.smsApi),
]
