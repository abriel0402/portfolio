from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("links/", views.links, name="links"),
]