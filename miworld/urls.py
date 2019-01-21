from django.contrib import admin
from django.urls import path, include
from .router import router
from .medias_router import medias_router
from django.views.decorators.csrf import csrf_exempt
from .post_router import post_router
from posts.post_api import urls as post_api_urls
from posts.comment_api import urls as comment_api_urls
from rest_framework.authtoken import views
from users.auth.login import LoginView
from users.auth.logout import LogoutView
from users.auth.register import RegisterView
from users.api.genericViews import ChangePasswordView
# from posts.post_api.generics import ActualPostView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('post_api/', include(post_router.urls)),
    path('media_api/', include(medias_router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api/password/', ChangePasswordView.as_view(), name='passwords'),
    path('post/', include(post_api_urls)),
    path('comment/', include(comment_api_urls)),
    path('rest-auth/', include('rest_auth.urls')),
    # path('posts/', ActualPostView.as_view(), name='posts'),


    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', csrf_exempt(RegisterView.as_view())),
]
