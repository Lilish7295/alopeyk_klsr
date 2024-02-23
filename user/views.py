from .models import CustomUser, CourierRequest
from .serializers import CustomUserSerializer, CourierRequestSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationApiView(generics.CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {'refresh':str(refresh),
                'access':str(refresh.access_token)}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourierRequestCreatview(generics.CreateAPIView):
    
    serializer_class = CourierRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        excisting_request = CourierRequest.objects.filter(status='pending').first()
        if not excisting_request:
            serializer.save(user=user)
    
   





