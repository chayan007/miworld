from rest_framework import views, mixins, generics
from medias.models import Image
from medias.image_api.serializers import ImageSerializer
from .serializers import PostSerializer

class ActualPost(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin):

    def get(self, request, id=None):
        post = self.retrieve(request, id)
        images = Image.objects.get(post=post)
        post_serializer = PostSerializer(post)
        image_serializer = ImageSerializer(images)


