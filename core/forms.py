from django import forms
from .models import Blog, Category
from tinymce.widgets import TinyMCE

class CreateBlog(forms.ModelForm):
    class Meta:
        model   = Blog
        fields  = ('blog_category', 'blog_title', 'blog_title_tag', 'blog_author', 'blog_body')
        widgets = {
            'blog_category'  : forms.Select(attrs={'class' : 'blog-category'}),
            'blog_title'     : forms.TextInput(attrs={'placeholder' : 'Title'}),
            'blog_title_tag' : forms.TextInput(attrs={'placeholder' : 'Title Tag'}),
            # 'blog_author'    : forms.Select(attrs={'placeholder' : 'Author'}),
            'blog_author'    : forms.TextInput(attrs={'id':'username', 'type':'hidden', 'value' : ''}),
            'blog_body'      : TinyMCE(attrs={'placeholder' : 'Blog Content ...'})
        }


class ContactForm(forms.Form):
    name    = forms.CharField(max_length=250, widget=forms.TextInput())
    email   = forms.EmailField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.Textarea())
    
    def send_email(self):
        pass

