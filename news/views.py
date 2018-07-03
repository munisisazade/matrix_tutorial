from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article


# Create your views here.


def index(request):
    obj = {}
    obj["news"] = Article.objects.all()
    return render(request, "index.html", obj)


def detail(request, id):
    obj = {}
    obj["object"] = Article.objects.get(id=id)
    Article.objects.all().delete()
    return render(request, "detail.html", obj)
