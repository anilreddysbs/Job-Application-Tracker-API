from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.urls')),  # Include job-related routes

    # JWT Authentication Routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login to get access & refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Get a new access token using refresh token
]
