from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user object"""

    class Meta:
        model = get_user_model()
        fields = ("id", "email", "phone_number", "password", "name")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5,
                "style": {"input_type": "password"},
            }
        }

    def create(self, validated_data):
        """ Create a new user with Encrypted password and return it """

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ Update user, setting data and return it """
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for user authentication object """

    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and Authenticate user"""
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )
        if not user:
            msg = "unable to authenticate with provided creds"
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs
