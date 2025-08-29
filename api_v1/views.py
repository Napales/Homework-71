from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import PostSerializer
from webapp.models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
