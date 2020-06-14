from rest_framework import serializers
from core.models import NetflixProfile


class NetflixProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetflixProfile
        fields = "__all__"
