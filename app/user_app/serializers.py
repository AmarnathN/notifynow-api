from rest_framework import serializers
from core.models import UserApp


class UserAppSerializer(serializers.ModelSerializer):
    """ Serializer for User App objetcs """

    class Meta:
        model = UserApp
        fields = ("id", "user", "app")
