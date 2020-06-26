from django.urls import path, include
from .views import UserAppAPIView, UserAppDetailsAPIView


urlpatterns = [
    path("", UserAppAPIView.as_view()),
    path("<int:id>/", UserAppDetailsAPIView.as_view()),
]
