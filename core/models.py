from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    category_slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse("Core:blog-category", kwargs={"category_slug": self.category_slug})

class Blog(models.Model):
    blog_title = models.CharField(max_length=350, verbose_name='Title', unique=True)
    blog_slug = models.SlugField(max_length=350)
    blog_title_tag = models.CharField(max_length=350, verbose_name='Title Tag')
    blog_body = models.TextField(verbose_name='Body')

    blog_author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Author')
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    blog_published = models.DateTimeField(auto_now_add=True)
    blog_updated   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.blog_title +" | "+ str(self.blog_author)
    
    def get_absolute_url(self):
        return reverse("Core:blog-detail", kwargs={"blog_slug": self.blog_slug})
    
    def save(self, *args, **kwargs): # new
        if not self.blog_slug:
            self.blog_slug = slugify(self.blog_title)
        return super().save(*args, **kwargs)

    def is_updated(self):
        state = False
        if self.blog_published == self.blog_updated:
            return self.blog_published
        else:
            return self.blog_updated





    
