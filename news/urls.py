from django.urls import path
from news.views import index, detail

urlpatterns = [
    path('', index, name="index"),
    path('news-detail/<int:id>/', detail, name="detail-news"),
]
