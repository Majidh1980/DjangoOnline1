from django.urls import path
from . import views


urlpatterns = [
    path('Login/', views.Login, name='login'),
    path('test/', views.test, name='test')
]