
from django.contrib import admin
from django.urls import path , include
from apii import views
from rest_framework.routers import DefaultRouter


# Creating Router Object

router = DefaultRouter()

# Register StudentViewSet with Router

router.register('stuapi', views.Student_Read_Only_modelViewSet, basename= 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
