from django.urls import path
from .generics import PostView
from .customAPI import ActualPost


urlpatterns = [
    path('post/<int:id>/', PostView.as_view(), name = 'post_detail'),
    path('post/', PostView.as_view(), name = 'post_list'),
    path('actual_post/', ActualPost.as_view(), name="actual_post"),

]