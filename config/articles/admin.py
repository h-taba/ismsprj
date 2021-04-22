from django.contrib import admin
from .models import Article, Comment,Organunit,Doctype,Ismsdoc


class CommentInline(admin.TabularInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comment)
admin.site.register(Organunit)
admin.site.register(Doctype)
admin.site.register(Ismsdoc)
