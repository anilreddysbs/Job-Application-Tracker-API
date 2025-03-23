from django.shortcuts import render
from rest_framework import generics,permissions,filters
from .models import JobApplication
from .serializers import JobSerializer, UserSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class JobListCreateAPIView(generics.ListCreateAPIView):
    serializer_class=JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'company_name', 'application_date']  # Filterable fields
    ordering_fields = ['application_date', 'company_name']  # Sorting fields
    search_fields = ['job_title', 'company_name']  # Allow searching by these fields

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)  # Only return jobs for the logged-in user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=JobSerializer
    permission_classes = [permissions.IsAuthenticated] 
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)  # Only return jobs for the logged-in user


class RegisteruserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Count
from rest_framework.decorators import api_view
def job_status_analytics(request):
    user=request.user
    if not user.is_authenticated:
        return Response({"error": "User not authenticated"}, status=status.HTTP_400_BAD_REQUEST)
    analytics = JobApplication.objects.filter(user=user).values('status').annotate(total=Count('status')).order_by('status')
    return Response(analytics)
