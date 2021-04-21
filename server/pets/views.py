from pets.models import Pet, Profile
from pets.serializers import PetSerializer, UserSerializer, ProfileSerializer, RegisterSerializer, RegisterShelterSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from pets.permissions import IsOwnerOrReadOnly, IsShelterOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class Login(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class RegisterShelterSerializerView(generics.CreateAPIView):
    queryset = User.objects.all()
    permissions_classes = [AllowAny]
    serializer_class = RegisterShelterSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PetSerializer

    def get_queryset(self):
        """
        Sets queryset to all Pet Objects. Then checks for query params of 'breed', 'type' , 'availability',
        'disposition', etc. If one of those is present, it alters the query according to that param and returns a new
        queryset with the Pet objects filtered by that. Can only accept one query param to filter by.
        """
        queryset = Pet.objects.all()

        # Tries to get data from the query params
        breed = self.request.query_params.get('breed')
        type = self.request.query_params.get('type')
        availability = self.request.query_params.get('availability')
        disposition = self.request.query_params.get('disposition')

        # Alters queryset according to the presence of a query param
        if breed is not None:
            queryset = queryset.filter(breed=breed)
        elif type is not None:
            queryset = queryset.filter(type=type)
        elif availability is not None:
            queryset = queryset.filter(availability=availability)
        elif disposition is not None:
            queryset = queryset.filter(disposition=disposition)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pets': reverse('pet-list', request=request, format=format),
    })
