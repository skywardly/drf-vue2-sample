from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]