from django.urls import path
from .views import JobListCreateAPIView, JobRetrieveUpdateDestroyAPIView, RegisteruserView,LogoutView
urlpatterns=[
    path('jobs/', JobListCreateAPIView.as_view(), name='job_list_create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='job_detail'),
    path('register/', RegisteruserView.as_view(), name='register_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]