from django.urls import path
from . import views
from .api import JobListAPI, JobDetailAPI

app_name = 'jobs'

urlpatterns = [
    # API
    path('job-list/', JobListAPI.as_view(), name='job-list-api'),
    path('job-list/<int:pk>/', JobDetailAPI.as_view(), name='job-list-api'),

    path('', views.job_list, name="job_list"),
    path('add/', views.add_job, name='add_job'),
    path('<str:slug>/', views.job_detail, name='job_detail'),


]
