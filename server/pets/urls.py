from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pets import views
from pets.views import Login, RegisterView, RegisterShelterSerializerView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.api_root),
    path('pets/', views.PetList.as_view(), name='pet-list'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('login/', Login.as_view(), name='login-token-pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('registershelter/', RegisterShelterSerializerView.as_view(), name='shelter_register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
