from rest_framework import serializers
from pets.models import Pet
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    pets = serializers.HyperlinkedRelatedField(many=True, view_name='pet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'pets']

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'gender', 'name', 'age', 'weight', 'type', 'breed', 'type', 'disposition', 'availability',
                  'description', 'picture_primary', 'picture_second', 'picture_third', 'owner']
        #                   'picture_second', 'picture_third'
