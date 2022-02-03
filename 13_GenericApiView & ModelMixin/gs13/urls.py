
from django.contrib import admin
from django.urls import path
from apii import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/',views.StudentList.as_view()),
    # path('stuapi/',views.StudentCreate.as_view()),
    # path('stuapi/<int:pk>',views.StudentRetrieve.as_view()),
    # path('stuapi/<int:pk>',views.StudentUpdate.as_view()),
    path('stuapi/<int:pk>',views.StudentDestroy.as_view()),
]
