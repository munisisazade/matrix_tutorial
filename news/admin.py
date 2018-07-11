from django.contrib import admin
from news.models import Article, Author


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'status', 'publish_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
