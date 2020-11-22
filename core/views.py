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
from .models import Blog

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
        context = super().get_context_data(**kwargs)
        context["message"]="ListView<br/>'get_context_data' method is overrided!"
        return context


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
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_context'] = "<i>'get_context_data method'</i> is overrided!"
        return context
    

class ArticleCreateView(CreateView):
    model         = Blog
    form_class    = CreateBlog
    template_name = 'add-blog.html'


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


from django.views.generic.edit import UpdateView

class ArticleUpdateView(UpdateView):
    model = Blog
    form_class = CreateBlog

    template_name_suffix = '_update_form'
    template_name = 'blog-update.html'
    

from django.views.generic.edit import DeleteView

class ArticleDeleteView(DeleteView):
    model = Blog
    template_name = 'blog-delete.html'
    success_url = reverse_lazy('Core:home')


from django.views.generic.dates import ArchiveIndexView

class ArticleIndexView(ArchiveIndexView):
    model = Blog
    if Blog.blog_published != Blog.blog_updated:
        date_field = 'blog_updated'
    else:
        date_field = 'blog_published'