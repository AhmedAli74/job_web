from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
    path('sign_up/',views.signup,name='signup'),
    path('login/',views.logiin,name='login'),
    path('logout/',views.logoutt,name='logout'),
    path('reset_password/',views.reset_password,name='reset_password'),
]