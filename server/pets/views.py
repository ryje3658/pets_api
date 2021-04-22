from pets.models import Pet, Profile
from pets.serializers import PetSerializer, UserSerializer, ProfileSerializer, RegisterSerializer, RegisterShelterSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from pets.permissions import IsOwnerOrReadOnly, IsShelterCanCreate
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class Login(TokenObtainPairView):
    """Allows anyone to Login via Post request. Returns a response with JWT."""
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    """Allows anyone to register as a normal user via Post request. Saves them as User in database."""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class RegisterShelterSerializerView(generics.CreateAPIView):
    """
    Allows anyone to register as a shelter user via Post request. Saves them as User in database with additional
    fields denoting their shelter status.
    """
    queryset = User.objects.all()
    permissions_classes = [AllowAny]
    serializer_class = RegisterShelterSerializer

class UserList(generics.ListAPIView):
    """Returns list of all user objects via GET request."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """Returns a single user object via GET request."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetList(generics.ListCreateAPIView):
    """
    Returns all pets via GET request. Creates a Pet object via a Post request when all necessary data is provided given
    the user attempting to create a pet is a user with shelter permissions. Will return a response with errors detailing
    any missing or invalid information, or if the user does not have shelter permissions.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsShelterCanCreate]
    serializer_class = PetSerializer

    def get_queryset(self):
        """
        Sets queryset to all Pet Objects. Then checks for query params of 'breed', 'type', 'availability',
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
    """
    An individual Pet object. Only owners of the Pet object are allowed to update or destroy the object. All other users
    can only retrieve the object.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """Allows users of API to click through links of API data from a central address."""
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pets': reverse('pet-list', request=request, format=format),
    })
