from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, Index
from . import views
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='update-detail'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='delete-detail'),
]
