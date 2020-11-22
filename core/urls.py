from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,

    ContactFormView,
    ArticleIndexView,
)

app_name = 'Core'

urlpatterns = [
    path('',                ArticleListView.as_view(),   name='home'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='blog-detail'),
    path('create/',         ArticleCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='blog-delete'),

    
    path('archive/', ArticleIndexView.as_view(template_name='blog-archive.html'), name='blog-archive'),
    path('cantact/', ContactFormView.as_view(), name='contact'),
]
