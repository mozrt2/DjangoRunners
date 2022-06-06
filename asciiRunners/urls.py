from django.urls import path
from . import views

urlpatterns = [
    path('', views.runner, name='index'),
    path('/results', views.results, name='results')
]