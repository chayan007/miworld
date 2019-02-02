from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import CommentSerializer, Comment
from django.contrib.auth.models import User
from notifications.models import Notification
from posts.models import Post


# class CommentView(generics.GenericAPIView,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin):
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#
#     def get(self, request, id=None):
#         if id:
#             post = Post.objects.get(id=id)
#             #return self.retrieve(request, id)
#             comments = Comment.objects.get(post=post)
#             return comments
#         else:
#             return Response({'error': 'No specific post is selected'})
#
#     def patch(self, request, id):
#         self.partial_update(request, id)
#         notification = Notification(user=User.objects.get(id=request.POST['user']), notification= 'edited a comment')
#         notification.save()
#         return Response({'status': 'success'})
#
#     def delete(self, request, id):
#         self.destroy(request, id)
#         notification = Notification(user=User.objects.get(id=request.POST['user']), notification='deleted a comment')
#         notification.save()
#         return Response({'status': 'success'})
#
class CommentView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, id=None):
        if id:
            post = Post.objects.get(id=id)
            comments = Comment.objects.get(post=post)
            return comments
        else:
            return Response({'error': 'No specific post is selected'})