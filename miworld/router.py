from products.api.viewsets import ProductModelViewSet
from users.api.viewsets import *
from followers.api.viewsets import FollowerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductModelViewSet)

router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)

router.register('followers', FollowerViewSet)