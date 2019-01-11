from django.urls import path
from .generics import PostView


urlpatterns = [
    path('post/<int:id>/', PostView.as_view(), name = 'post_detail'),
    path('post/', PostView.as_view(), name = 'post_list'),

]