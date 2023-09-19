from django.urls import path
from . import views


urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("create_article", views.create_article, name="create_article"),
    path("<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),  # pk - primary key
    path("<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"),
]
