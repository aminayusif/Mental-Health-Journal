from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from journal.views_auth import MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/journal/', include('journal.urls')),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]