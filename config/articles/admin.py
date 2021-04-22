from django.contrib import admin
from .models import Article, Comment,Office,Doctypes


class CommentInline(admin.TabularInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comment)
admin.site.register(Office)
admin.site.register(Doctypes)

