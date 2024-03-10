from .models import Package, Feedback
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ['id', 'origin_long', 'origin_lat',
            'destination_long', 'destination_lat', 'status',
            'pick_date', 'customer', 'courier', 'condition']


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = "__all__"