from django.urls import path
from notify import views

app_name = "notify"

urlpatterns = [path("", views.NotifyView.as_view())]
