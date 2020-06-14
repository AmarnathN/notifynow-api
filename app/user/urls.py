from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("", views.ListUsersView.as_view()),
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("<int:id>/", views.UpdateUserView.as_view(), name="update"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
]
