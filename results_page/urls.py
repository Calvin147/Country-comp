from django.urls import path
from . import views

app_name = 'results_page'
urlpatterns = [
    path('vote/<str:country_name>/', views.vote_for_country, name='vote_for_country'),
    path('results/', views.results, name='results'),
]