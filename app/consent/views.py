from rest_framework import generics, mixins
from .serializers import ConsentSerializer
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from core.models import Consent

# Create your views here.
class ConsentAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
):
    serializer_class = ConsentSerializer
    queryset = Consent.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# Update your views here.
class ConsentDetailsAPIView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ConsentSerializer
    queryset = Consent.objects.all()
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        return self.retrieve(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
