from django.contrib import admin
from news.models import Article, Author


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('title',)
    list_display = ('title', 'order', 'status', 'publish_date')


# admin.site.register(Article, ArticleAdmin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('get_image',)
    list_display = ('get_image',)
