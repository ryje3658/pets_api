from rest_framework import serializers
from pets.models import Pet, Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['is_shelter']


class UserSerializer(serializers.ModelSerializer):
    pets = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'pets', 'profile']


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'gender', 'name', 'age', 'weight', 'type', 'breed', 'type', 'disposition', 'availability',
                  'description', 'picture_primary', 'picture_second', 'picture_third', 'owner']
