from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .models import City


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True) # to prevent user of reading password
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already registered.'})

        account = User(username=self.validated_data['username'],
                       email=self.validated_data['email'])

        account.set_password(password)
        account.save()

        return account


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class ChangableUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def validatate_email(self, email):
        if '@' not in email or '.' not in email:
            raise serializers.ValidationError({'email': 'Invalid email address.'})
        return email


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class ProfileSerializer(serializers.ModelSerializer):
    user = ChangableUserSerializer()
    city = CitySerializer()
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'city', 'image']
        