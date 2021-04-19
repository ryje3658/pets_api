from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pets import views

urlpatterns = [
    path('', views.api_root),
    path('pets/', views.PetList.as_view(), name='pet-list'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
