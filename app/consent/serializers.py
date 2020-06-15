from rest_framework import serializers
from core.models import Consent


class ConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consent
        fields = "__all__"
