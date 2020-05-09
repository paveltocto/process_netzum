from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    url(r'^books/', include('application.api.books.routers')),
]

urlpatterns += router.urls
