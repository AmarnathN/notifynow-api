from django.shortcuts import render


from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import UserMail
from user_mail import serializers

# Create your views here.


class UserMailViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin
):
    """ Manage database for User Mail details """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = UserMail.objects.all()
    serializer_class = serializers.UserMailSerializer

    def get_queryset(self):
        """ return objects fro current authenticated users only """
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ Create a new user mail """
        serializer.save(user=self.request.user)
