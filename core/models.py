from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=350, verbose_name='Title', unique=True)
    blog_title_tag = models.CharField(max_length=350, verbose_name='Title Tag')
    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Author')
    blog_body = models.TextField(verbose_name='Body')

    blog_published = models.DateTimeField(auto_now_add=True)
    blog_updated   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title +" | "+ str(self.blog_author)
    
    def get_absolute_url(self):
        return reverse("Core:blog-detail", kwargs={"pk": self.pk})

    def is_updated(self):
        state = False
        if self.blog_published == self.blog_updated:
            return self.blog_published
        else:
            return self.blog_updated





    
