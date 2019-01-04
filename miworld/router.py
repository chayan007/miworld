from products.api.viewsets import ProductViewSet, ProductModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products_model', ProductModelViewSet)
router.register('products', ProductViewSet, base_name='product')

for url in router.urls:
    print(url)