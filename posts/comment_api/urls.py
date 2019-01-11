from django.urls import path
from .generics import CommentView

urlpatterns = [
    path('comment/<int:id>/', CommentView.as_view(), name = 'comment_detail'),
    path('comment/', CommentView.as_view(), name = 'comment_list'),
]