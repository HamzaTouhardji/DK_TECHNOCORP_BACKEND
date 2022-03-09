from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.shortcuts import render
from users.models import NewUser
from rest_framework import viewsets
from django.http import HttpResponse


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = []
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                account.is_active = True
                account.save()
                token = RefreshToken.for_user(account)
                return HttpResponse(token, content_type="application/json")

            else:
                data = serializer.errors

                return Response(data)
        except KeyError as e:
            print(e)
            raise Response({"400": f'Field {str(e)} missing'})


class Users(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, UpdateEntreprisePermission]
    #permission_classes = [UpdateEntreprisePermission]
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
