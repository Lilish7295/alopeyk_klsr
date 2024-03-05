from django.urls import path
from .views import PackageView, TripCostView, CanselOrderView


urlpatterns = [

    path('package/view/', PackageView.as_view(),
        name='pakage_view'),

    path('trip/cost/', TripCostView.as_view(),
        name='trip_cost'),

    path('cansel/order/', CanselOrderView.as_view(),
        name='cansel_order'),

]