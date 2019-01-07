from posts.post_api.viewsets import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', PostViewSet)