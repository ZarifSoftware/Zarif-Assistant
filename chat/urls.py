from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('get', views.response, name='response'),
    path('contact', views.contact, name="contact"),
    path('con', views.con, name="con"),
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("bot", views.bot, name="bot"),
    path("weather", views.weather, name="weather"),
    path('get_weather', views.get_weather, name="getWeatherResponse")
]
