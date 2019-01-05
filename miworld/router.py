from products.api.viewsets import ProductViewSet, ProductModelViewSet
from users.api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products_model', ProductModelViewSet)
router.register('products', ProductViewSet, base_name='product')

router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)