from django.urls import path, include
from .views import NetflixProfileAPIView, NetflixProfileDetailsAPIView


urlpatterns = [
    path("", NetflixProfileAPIView.as_view()),
    path("<int:id>/", NetflixProfileDetailsAPIView.as_view()),
]
