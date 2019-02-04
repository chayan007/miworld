from rest_framework.decorators import api_view
from .serializers import Like
from posts.models import Post
from users.models import Profile
from django.http import JsonResponse
from users.api.serializers import LikerSerializer


@api_view(['GET', ])
def get_liker(request, id):
    post = Post.objects.get(id=id)
    likes = Like.objects.filter(post=post)
    liker_list = {}
    count = 0
    for like in likes:
        liker = Profile.objects.get(user=like.user)
        liker_serializer = LikerSerializer(liker)
        liker_list[count] = liker_serializer.data
        count = count+1
    return JsonResponse(liker_list)
