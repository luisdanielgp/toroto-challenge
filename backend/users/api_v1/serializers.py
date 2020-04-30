from django.contrib.auth import authenticate

from rest_framework import serializers

from subscriptions.api_v1.serializers import SubscriptionSerializer

from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    This serializer provides the CustomUser fields needed for it's creation
    """
    subscription = SubscriptionSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'co2_tons_per_year',
            'subscription'
        )
        extra_kwargs = {
            'username': {'read_only': True},
            'co2_tons_per_year': {'required': True}
        }
        partial = True


class LogInSerializer(serializers.Serializer):
    """ Serializer for user Login """
    email = serializers.CharField(label="Email")
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs