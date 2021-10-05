from django.urls import path
from .views import get_by_manufactor, get_all


try:
    from django.urls import path

    urlpatterns = [
        path('app-versions/', get_all, name='index'),
        path('app-versions/<str:manufactor>', get_by_manufactor, name='get by manufactor'),
    ]
except:
    from django.conf.urls import  url

    urlpatterns = [
        url(r'app-versions/', get_all, name='index'),
        url(r'app-versions/<str:manufactor>', get_by_manufactor, name='get by manufactor'),
    ]
