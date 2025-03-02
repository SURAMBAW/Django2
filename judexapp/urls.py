from django.urls import path

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns=[
    path ('judexapp/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path ('judexapp/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
]