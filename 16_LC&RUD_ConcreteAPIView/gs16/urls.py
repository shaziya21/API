
from django.contrib import admin
from django.urls import path
from apii import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/',views.StudentListCreate.as_view()),
    path('stuapi/<int:pk>',views.StudentRetrieveUpdateDestroy.as_view()),

]
