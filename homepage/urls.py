
from django.conf.urls import url
from . import views
from homepage.views import this
urlpatterns = [
    url(r'^$', views.home),
    url(r'^sync', views.sync)
]