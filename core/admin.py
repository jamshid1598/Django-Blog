from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import (
    Category,
    Blog,
)

# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    ordering     = ('category_name',)

    prepopulated_fields = {'category_slug': ('category_name',)}


admin.site.register(Category, BlogCategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display       = ('blog_category', 'blog_title', 'blog_title_tag', 'blog_author', 'blog_published', 'blog_updated', )
    list_display_links = ( 'blog_title',)
    list_editable      = ('blog_category', 'blog_title_tag', 'blog_author')
    ordering           = ('blog_category', 'blog_title', 'blog_author', 'blog_published', 'blog_updated',)
    search_fields      = ('blog_category', 'blog_title', 'blog_title_tag', 'blog_author')

    prepopulated_fields = {'blog_slug': ('blog_title',)}

    fieldsets = (
        (
            'Category', {
                'fields' : (
                    'blog_category',
                )
            }
        ),
        (
            'Blog Content', {
                'fields' : ('blog_title', 'blog_slug', 'blog_title_tag', 'blog_body', 'blog_author',)
            }
        )
    )

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(Blog, BlogAdmin)
