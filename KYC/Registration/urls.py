from django.urls import path , include

from . import views

app_name = "Registration"

urlpatterns = [
    path("" ,views.Register , name='Register'),
]