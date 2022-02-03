
from django.contrib import admin
from django.urls import path , include
from apii import views
from rest_framework.routers import DefaultRouter


# Creating Router Object

router = DefaultRouter()

router.register('stuapi', views.SingerViewSet, basename= 'singer')
router.register('song', views.SongViewSet, basename= 'song')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]
