from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article
from news.forms import ArticleForm


# Create your views here.


def index(request):
    if request.method == 'GET':
        obj = {}
        obj["form"] = ArticleForm()
        obj["news_list"] = Article.objects.all()
        return render(request, "index.html", obj)
    else:
        context = {}
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Article.objects.create(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description']
            # )
            article = form.save()
        context["news_list"] = Article.objects.all()
        context["form"] = form
        return render(request, "index.html", context)


def detail(request, name):
    obj = {}
    obj["object"] = Article.objects.get(id=name)
    return render(request, "detail.html", obj)
