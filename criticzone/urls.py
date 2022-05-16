from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
     path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('media/favicon.ico'))),
    path('', views.index, name="index"),
]
