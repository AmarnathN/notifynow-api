from django.urls import path, include
from .views import ConsentAPIView, ConsentDetailsAPIView


urlpatterns = [
    path("", ConsentAPIView.as_view()),
    path("<int:id>/", ConsentDetailsAPIView.as_view()),
]
