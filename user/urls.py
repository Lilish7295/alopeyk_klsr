from django.urls import path
from .views import UserRegistrationApiView, CourierRequestCreatview


urlpatterns = [

    path('api/register/', UserRegistrationApiView.as_view(),
        name='user_registration'),

    path('api/courier/request/', CourierRequestCreatview.as_view(),
         name='courier_request' ),

]