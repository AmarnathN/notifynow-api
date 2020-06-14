from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("<int:id>/", views.UpdateUserView.as_view(), name="update"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
]
