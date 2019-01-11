from posts.post_api.viewsets import PostViewSet
from posts.like_api.viewsets import LikeViewSet
from posts.comment_api.viewsets import CommentViewSet
from rest_framework import routers
from django.urls import path

post_router = routers.DefaultRouter()

post_router.register('posts', PostViewSet)
post_router.register('likes', LikeViewSet)
post_router.register('comments', CommentViewSet)

# urlpatterns = [
#     path(),
# ]
