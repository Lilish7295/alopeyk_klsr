from django.urls import path
from .views import TokenObtainPairView, UserRegistrationApiView, TokenRefreshPairView


urlpatterns = [

    path('api/register/', UserRegistrationApiView.as_view(),
          name='user_registration'),
          
]