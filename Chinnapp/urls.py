from django.urls import path 
from Chinnapp import views 

urlpatterns = [
    path('',views.chinna_view,name="chinna")
]
