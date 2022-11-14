from django.urls import path

from .views import family,selection

urlpatterns=[
    path("family/",family,name="family"),
    path("selection/<int:id>/",selection,name="selection"),
]