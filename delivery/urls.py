from django.urls import path
from .views import PackageView, TripCostView


urlpatterns = [

    path('package/view/', PackageView.as_view(),
        name='pakage_view'),

    path('trip/cost/', TripCostView.as_view(),
        name='trip_cost'),

]