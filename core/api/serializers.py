from rest_framework.serializers import ModelSerializer

from core.models import Blog

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = [
            'blog_title',
            # 'blog_slug',
            'blog_body',
            'blog_category',
        ]


"""

data = {
    'blog_title': "new sport",
    'blog_body': 'this is not lorem epson, this is simple text for blog body',
    'blog_category': category.pk,
}

"""