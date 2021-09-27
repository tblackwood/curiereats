from core.models import Courier
from django.urls import path
from . import views, apis as courier_api


urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/available/', views.available_jobs_page, name='available_jobs'),
    path('jobs/available/<id>/', views.available_job_page, name='available_job'),
    path('jobs/current/', views.current_job_page, name='current_job'),
    path('jobs/current/<id>/take_photo', views.current_job_take_photo_page, name='current_job_take_photo'),
    path('jobs/complete/', views.job_complete_page, name='job_complete'),
    path('jobs/archived/', views.archived_jobs_page, name='archived_jobs'),
    path('profile/', views.profile_page, name='profile'),
    path('payout_method/', views.payout_method_page, name='payout_method'),

    #API urls
    path('api/jobs/available/', courier_api.available_jobs_api, name='available_jobs_api'),
    path('api/jobs/current/<id>/update/', courier_api.current_job_update_api, name='current_job_update_api'),
    path('api/fcm-token/update/', courier_api.fcm_token_update_api, name="fcm_token_update_api"),

]