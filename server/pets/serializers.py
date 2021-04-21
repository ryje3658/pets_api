from rest_framework import serializers
from pets.models import Pet, Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile object. Extends base User model with fields relevant to status and shelter attributes.
    """
    class Meta:
        model = Profile
        fields = ['is_shelter', 'shelter_name', 'shelter_bio']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User object. Can only have pets if they are a shelter.
    """
    pets = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'pets', 'profile']


class PetSerializer(serializers.ModelSerializer):
    """
    Serializer for Pet object. Owner refers to the shelter that owns the pet.
    """
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'gender', 'name', 'age', 'weight', 'type', 'breed', 'type', 'disposition', 'availability',
                  'description', 'picture_primary', 'picture_second', 'picture_third', 'owner']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for JWT tokens. Generated when user logs in.
    """
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims to include in generated token
        token['username'] = user.username
        token['is_shelter'] = user.profile.is_shelter
        return token


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for normal User object with no special permissions.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        """When we send a post request to register endpoint, this method is called which saves User."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class RegisterShelterSerializer(serializers.ModelSerializer):
    """
    Creates a User object, and updates the user.profile object attribute of is_shelter to True. Also uses the given
    username as the name of the shelter.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        """When we send a post request to register endpoint, this method is called which saves User."""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        # Update profile object to reflect status as a shelter.
        profile = Profile.objects.get(pk=user.id)
        profile.is_shelter = True
        profile.shelter_name = validated_data['username']

        profile.save()

        return user
