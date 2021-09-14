from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'), 
]