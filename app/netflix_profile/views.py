from rest_framework import generics, mixins
from .serializers import NetflixProfileSerializer
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from core.models import NetflixProfile

# Create your views here.
class NetflixProfileAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
):
    serializer_class = NetflixProfileSerializer
    queryset = NetflixProfile.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# Create your views here.
class NetflixProfileDetailsAPIView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = NetflixProfileSerializer
    queryset = NetflixProfile.objects.all()
    lookup_field = "id"
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)