from medias.image_api.viewsets import ImageViewSet
from rest_framework import routers
from django.urls import path

medias_router = routers.DefaultRouter()

medias_router.register('posts', ImageViewSet, base_name='posts')

# urlpatterns = [
#     path(),
# ]
