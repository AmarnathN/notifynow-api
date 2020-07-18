from django.urls import path, include
from .views import NotificationAPIView, NotificationDetailsAPIView


urlpatterns = [
    path("", NotificationAPIView.as_view()),
    path("<int:id>/", NotificationDetailsAPIView.as_view()),
]
