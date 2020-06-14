from django.urls import path, include
from .views import NetflixProfileAPIView, NetflixProfileDetailsAPIView


urlpatterns = [
    path("user/netflix_profiles/", NetflixProfileAPIView.as_view()),
    path("user/netflix_profiles/<int:id>/", NetflixProfileDetailsAPIView.as_view()),
]
