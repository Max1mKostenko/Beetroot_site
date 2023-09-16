from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("about", views.about, name="about"),
    path("contacts", views.contacts, name="contacts"),
    path("test_1", views.test_1, name="test_1"),
    path("test_2", views.test_2, name="test_2"),
    path("test_3", views.test_3, name="test_3"),
]
