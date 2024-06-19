from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('smart_home', views.smart_page, name='smart'),
    path('profile', views.profile_view, name='profile'),
]