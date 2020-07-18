from rest_framework import serializers
from core.models import UserMail


class UserMailSerializer(serializers.ModelSerializer):
    """ Serializer for User mail objetcs """

    class Meta:
        model = UserMail
        fields = ields = "__all__"
