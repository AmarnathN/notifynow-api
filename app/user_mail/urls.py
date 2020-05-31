from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_mail import views


router = DefaultRouter()
router.register("user_mails", views.UserMailViewSet)

app_name = "user_mail"

urlpatterns = [path("", include(router.urls))]
