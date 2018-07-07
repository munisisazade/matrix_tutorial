from django.urls import path, re_path
from news.views import index, detail

app_name = 'news'

urlpatterns = [
    path('', index, name="index"),
    path('news-detail/<int:name>/', detail, name="detail-news"),
]
