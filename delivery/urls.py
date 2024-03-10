from django.urls import path
from .views import PackageView, TripCostView, CreateOrder, CanselOrder, OrderListView


urlpatterns = [

    path('package/view/', PackageView.as_view(),
        name='pakage_view'),

    path('trip/cost/', TripCostView.as_view(),
        name='trip_cost'),

    path('create/order/', CreateOrder.as_view(),
        name='create_order'),

    path('cansel/order/<int:pk>/', CanselOrder.as_view(),
        name='cansel_order'),

    path('order/list/', OrderListView.as_view(),
        name='order_list_view'),

]