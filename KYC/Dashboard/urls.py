from django.urls import path
from . import views

app_name = "Dashboard"


urlpatterns = [
    path("Dash/" ,views.Dash , name='Dash'),
]