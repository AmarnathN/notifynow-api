from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import User

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """

    serializer_class = UserSerializer


class ListUsersView(generics.ListAPIView):
    """ Create a new user in the system """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class CreateTokenView(ObtainAuthToken):
    """ Create a new Auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UpdateUserView(generics.RetrieveUpdateAPIView):
    """ Manage the authenticated user """

    serializer_class = UserSerializer
    lookup_field = "id"
    queryset = User.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """ Retieve and return authenticated user"""
        return self.request.user
