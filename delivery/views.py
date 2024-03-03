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

    def process_mapbox_response(self, response):
        
        cost_per_kilometer = 10000
        distance_data = response.json()
        total_cost = distance_data["routes"][0]["legs"][0]["distance"]["value"]/1000*cost_per_kilometer
        return total_cost
    
    def get_weather_condition(self):

        city = 'Tehran,ir'
        api_key = 'e03d7f8b738bab332d03ceb18646d6a0'
        base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url=base_url)
        data = response.json()
        weather_condition = 'bad' if any(keyword in data['weather'][0]['description'] for keyword in ['rain', 'snow']) else 'good'
        return weather_condition

    def post(self, request):

        try:
            type = request.data.get('type')
            origin = request.data.get('origin')
            destination = request.data.get('destination')
            mapbox_url = f"https://api.neshan.org/v4/direction?type={type}&origin={origin}&destination={destination}"
            headers = {'Api-key': 'service.308a316f9ab1485183a8508d8437291a',
                'X-CSRFToken': 'CSRF Token'}
            response = requests.get(mapbox_url, headers=headers, verify=False)
            total_cost = self.process_mapbox_response(response)
            weather_condition = self.get_weather_condition()
            pick_date = timezone.now()
            if weather_condition == 'bad':
                total_cost +=10000
            return Response({'total_cost':total_cost, 'weather':weather_condition,
                'date':pick_date}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

