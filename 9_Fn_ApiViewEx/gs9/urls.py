
from django.contrib import admin
from django.urls import path
from api1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/', views. hello_world),
]
