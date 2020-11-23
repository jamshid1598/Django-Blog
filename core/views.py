from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from .forms import CreateBlog #UpdateBlog
from .models import Blog, Category

# Create your views here.

class ArticleListView(ListView):

    """
    
    method flowchart:

    setup()
    dispatch()
    get_template_names()
    get_context_object_name()
    get_context_data()
    get_queryset()
    http_method_not_allowed()
    get()
    render_to_response()

    """

    paginate_by   = 5
    model         = Blog
    template_name = 'index.html'
    ordering = ('-blog_published')

    def get_context_data(self, **kwargs):
        context             = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def get_queryset(self, *args, **kwargs):
        kwargs_key = [key  for key in self.kwargs]
        if 'category_slug' in kwargs_key:
            return Blog.objects.filter(blog_category__category_slug=self.kwargs['category_slug'])
        else:
            return Blog.objects.all()


class ArticleDetailView(DetailView):
  
    """
    Method flowchart:

    setup(),
    dispatch(),
    get_template_names(),
    get_context_object_name(),
    get_context_data(),
    get_object(),
    http_method_not_allowed(),
    get(),
    render_to_response(),
    """
    
    model = Blog
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    template_name = 'blog-detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kwargs_key = [key for key in self.kwargs]
        print(kwargs_key)
        # context['extra_context'] = 
        return context
    

class ArticleCreateView(CreateView):
    model         = Blog
    form_class    = CreateBlog
    template_name = 'add-blog.html'


class ArticleUpdateView(UpdateView):
    model = Blog
    form_class = CreateBlog
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'

    template_name_suffix = '_update_form'
    template_name = 'blog-update.html'
    
class ArticleDeleteView(DeleteView):
    model = Blog
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    template_name = 'blog-delete.html'
    success_url = reverse_lazy('Core:home')


# from django.views.generic.edit import FormView
from django.views.generic import FormView
from .forms import ContactForm

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'Core:home'
    
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form) 


from django.views.generic.dates import ArchiveIndexView
class ArticleIndexView(ArchiveIndexView):
    model = Blog
    if Blog.blog_published != Blog.blog_updated:
        date_field = 'blog_updated'
    else:
        date_field = 'blog_published'