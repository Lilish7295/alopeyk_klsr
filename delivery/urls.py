from django.urls import path
from .views import PackageView


urlpatterns = [

    path('package/view/', PackageView.as_view(),
        name='pakage_view'),

]