from django.db import models
from django.contrib import admin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model): # new
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments', # new
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')


class Doctype(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Organunit(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
class Ismsdoc(models.Model): # new
    doctitle = models.CharField(max_length=150)                                             
    Organunit_fk = models.ForeignKey(
        Organunit,
        on_delete=models.CASCADE,
        related_name='docs_of_office', # new
    )
    version =models.IntegerField()
    serial=models.IntegerField()
    codeexperision=models.CharField(max_length=20)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='docs_of_auther'
    )

    def __str__(self):
        return self.doctitle

    def get_absolute_url(self):
        return reverse('article_list')





class Employee(models.Model):
    lastname = models.CharField("Last", max_length=64)
    firstname = models.CharField("First", max_length=64)
    middlename = models.CharField("Middle", max_length=64)
    clocknumber = models.CharField(max_length=16)

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s-%s-%s' % (self.lastname, self.firstname, self.middlename)
    full_name = property(_get_full_name)


    class Meta:
        ordering = ['lastname','firstname', 'middlename']






