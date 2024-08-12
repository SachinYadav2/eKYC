from django.urls import path
from . import views

app_name = 'Login'

urlpatterns = [
    path('login/' , views.Login , name='login'),

]