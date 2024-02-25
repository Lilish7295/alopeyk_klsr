from django.urls import path
from .views import UserRegistrationApiView, CourierRequestCreatview, UserDetail, NormalUserDetail, CourierUserDetail


urlpatterns = [

    path('api/register/', UserRegistrationApiView.as_view(),
        name='user_registration'),

    path('api/courier/request/', CourierRequestCreatview.as_view(),
        name='courier_request' ),

    path('api/user/detail/<int:pk>/', UserDetail.as_view(), 
        name='user_detail'),

    path('api/normal/detail/<int:pk>/', NormalUserDetail.as_view(),
        name='normal_user_detail'),

    path('api/courier/detail/<int:pk>/', CourierUserDetail.as_view(),
        name="courier_user_detail"),

]