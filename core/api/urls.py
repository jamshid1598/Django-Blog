from django.urls import path
from .views import (
    BlogListAPIView,
)

app_name = 'blog-api'

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blog-api-list'),
    # path('blog/<slug:category_slug>/', ArticleListView.as_view(), name='category'),

    # path('detail/<slug:blog_slug>', ArticleDetailView.as_view(), name='blog-detail'),
    # path('create/', ArticleCreateView.as_view(), name='blog-create'),
    # path('update/<slug:blog_slug>/', ArticleUpdateView.as_view(), name='blog-update'),
    # path('delete/<slug:blog_slug>/', ArticleDeleteView.as_view(), name='blog-delete'),

    # path('blog-like/<slug:blog_slug>/', BlogPostLikes, name='blog-like'),

    
    # path('archive/', ArticleIndexView.as_view(template_name='blog-archive.html'), name='blog-archive'),
    # path('cantact/', ContactFormView.as_view(), name='contact'),
]
