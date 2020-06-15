from rest_framework import generics, mixins
from .serializers import ForwardMailIdSerializer
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from core.models import ForwardMailId

# List your views here.
class ForwardMailIdAPIView(
    generics.GenericAPIView, mixins.ListModelMixin,
):
    serializer_class = ForwardMailIdSerializer
    queryset = ForwardMailId.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
