from django.urls import path
from .views import TokenObtainPairView, UserRegistrationView,UserProfileView, UpdateUserProfileView


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(),
          name='token_obtain_pair'),
    path('api/register/', UserRegistrationView.as_view(),
          name='user_registration'),
    path('api/profile/', UserProfileView.as_view(),
          name='user_profile'),
    path('api/profile/update/', UpdateUserProfileView.as_view(), 
         name='update_user_profile')
]