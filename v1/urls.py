from django.urls import path
from . import views

urlpatterns = [
    path("lyceum/", views.lyceum, name="lyceum"),
    path("lyceum/push/", views.push, name="push"),
]
