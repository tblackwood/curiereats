from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home, name='home'),
    #path('profile/', views.profile_page, name='profile'),
    path('', views.home, name='home')
]