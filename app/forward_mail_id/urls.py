from django.urls import path, include
from .views import ForwardMailIdAPIView


urlpatterns = [
    path("", ForwardMailIdAPIView.as_view()),
]
