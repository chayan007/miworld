from django.contrib import admin
from django.urls import path, include
from .router import router
from .post_router import post_router
from posts.post_api import urls as post_api_urls
from posts.comment_api import urls as comment_api_urls
from rest_framework.authtoken import views
from users.api.genericViews import ChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('post_api/', include(post_router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api/password/', ChangePasswordView.as_view(), name='passwords'),
    path('post/', include(post_api_urls)),
    path('comment/', include(comment_api_urls))
]
