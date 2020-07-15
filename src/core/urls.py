from django.urls import path
from . import views
urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='CSCL-home'),
    path('about/', views.about, name='CSCL-about'),
    path('suggestions/', views.suggestions, name='CSCL-suggestions'),
    path('forum/', views.forum, name='CSCL-forum'),   
]
