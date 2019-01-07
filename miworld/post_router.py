from posts.post_api.viewsets import PostViewSet
from posts.like_api.viewsets import LikeViewSet
from posts.comment_api.viewsets import CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('', PostViewSet)
router.register('likes', LikeViewSet)
router.register('comments', CommentViewSet)