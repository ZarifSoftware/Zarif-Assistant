from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls'))

]
admin.site.site_header = "Welcome to Zarif's Chatbot's Admin"
admin.site.site_title = "Zarif's Chatbot's Admin"
admin.site.index_title = "Zarif's Chatbot's Admin"
