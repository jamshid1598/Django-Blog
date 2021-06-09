from rest_framework.generics import ListAPIView

from core.models import Blog

from .serializers import BlogSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer