from rest_framework import serializers
from core.models import ForwardMailId


class ForwardMailIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardMailId
        fields = "__all__"
