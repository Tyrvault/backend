

from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bandas.views import EventoViewSet
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from rest_framework_simplejwt.views import TokenVerifyView


router = routers.DefaultRouter()
router.register(r'patobands', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('bandas.urls')),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
       
]
