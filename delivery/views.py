from django.conf import settings
import requests
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions, serializers
from .models import Package
from .serializers import PackageSerializer


class PackageView(APIView):
    
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        partial = True
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TripCostView(APIView):

    MAP_BOX_DIRECTION_API_URL = 'https://api.neshan.org/v4/direction?type=X&origin=A&destination=B'
    def process_mapbox_respons(self, respons):
        
        api_key = 'service.308a316f9ab1485183a8508d8437291a'
        base_url = settings.BASE_URL
        cost_per_kilometer = 3000
        total_cost = respons.json()['routes'][0]['distance']/1000*cost_per_kilometer
        headers = {
            'X-CSRFToken': 'CSRF Token',
            'Api-key': 'service.308a316f9ab1485183a8508d8437291a',
            'Content-Type': 'application/json'
        }
        params = {
            'origin' : '{},{}'.format((respons.json()['waypoints'][0]['location'][1]),
                (respons.json()['waypoints'][0]['location'][0])),
            'destination' : '{},{}'.format((respons.json()['waypoints'][1]['location'][1]),
                (respons.json()['waypoints'][1]['location'][0])),
        }
        distance_response = requests.get(base_url, headers=headers, params=params)
        distance_data = distance_response.json()
        return distance_data
    
    def get_weather_condition(self, latitud, longitud):

        api_key = '58d1fb0dbc6c6790007a4fa59ec1d973'
        base_url = 'https://home.openweathermap.org/'
        params = {
            'lat' : latitud,
            'lon' : longitud,
            'appid' : api_key
        }
        weather_response = requests.get(base_url, params=params)
        weather_data = weather_response.json()
        weather_condition = 'bad' if any(keyword in 
            weather_data['weather'][0]['description'].lower() 
            for keyword in ['rain', 'snow']) else 'good'
        return weather_condition
    
    def is_holiday(self, pick_date):

        api_key = 'https://api.keybit.ir/time'
        base_url = 'https://api.keybit.ir/time/?timezone=asia/tehran'
        params = {
            'year' : pick_date.year,
            'month' : pick_date.month,
            'day' : pick_date.day,
            'key' : api_key
        }
        holiday_response = requests.get(base_url, params=params)
        holiday_data = holiday_response.json()
        is_holiday = holiday_data['holiday']
        return is_holiday
    
    def is_in_tehran(latitud, longitud):

        tehran_longitud_range = (51.22,51.73)
        tehran_latitud_range = (35.42,35.90)
        is_in_longitud_range = tehran_longitud_range[0] <= longitud <= tehran_longitud_range[1]
        is_in_latitud_range = tehran_latitud_range[0] <= latitud <= tehran_latitud_range[1]
        return is_in_longitud_range and is_in_latitud_range
    
    def post(self, requst):

        try:
            origin_lat = requst.data.get('origin_lat')
            origin_long = requst.data.get('origin_long')
            destination_lat = requst.data.get('destination_lat')
            destination_long = requst.data.get('destination_long')
            origin = '{},{}'.format(origin_lat, origin_long)
            destination = '{},{}'.format(destination_lat,destination_long)
            mapbox_api_key = 'service.308a316f9ab1485183a8508d8437291a'
            url = self.MAP_BOX_DIRECTION_API_URL.format(origin=origin,
                destination=destination, api_key=mapbox_api_key)
            response = requests.get(url)
            print(response.json())
            distance_data = self.process_mapbox_respons(response)
            origin_weather_condition = self.get_weather_condition(origin)
            destination_weather_condition = self.get_weather_condition(destination)
            total_cost = self.process_mapbox_respons(response)
            pick_date = timezone.now()
            
            if self.is_holiday(pick_date) or origin_weather_condition == 'bad' or destination_weather_condition == 'bad':
                total_cost += 5000

            new_package = Package(
                origin = origin,
                destination = destination,
                pick_date = timezone.now(),
                customer = requst.user.customer,
                courier = None,
                condition = 'wating'
            )
            new_package.save()

            if not (self.is_in_tehran(float(origin_long),
                float(origin_lat) and self.is_in_tehran(float(destination_long),
                float(destination_lat)))):
                return Response({'error':'مبدا یا مقصد خارج از محدوده‌ی تهران است'},
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'total_cost':total_cost, 'distance_data':distance_data,
                    'package_id':new_package.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

