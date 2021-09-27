from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_page, name='profile'),
    path('payment_method/', views.payment_method_page, name='payment_method'),
    path('create_job/', views.create_job_page, name='create_job'),
    path('jobs/current/', views.current_jobs_page, name='current_jobs'),
    path('jobs/archived/', views.archived_jobs_page, name='archived_jobs'),
    path('jobs/<job_id>/', views.job_page, name='job'),
    
]   