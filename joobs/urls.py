from django.urls import path
from . import views
app_name='joobs'
urlpatterns = [
    path('',views.job,name='jobs'),
    path('post_job/',views.add_job,name='post_job'),
    path('<str:job_slug>/',views.job_details,name='job_slug'),
    
]