from django.shortcuts import render
from rest_framework import generics
from backend.models import Entreprise
from .serialisers import EntrepriseSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class UpdateEntreprisePermission(BasePermission):
    message = 'Updating entreprises is restricted to the founder only.'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.founder == request.users


# class EntrepriseList(generics.ListCreateAPIView):
class EntrepriseList(viewsets.ModelViewSet):
   # permission_classes = [
    #     IsAuthenticated, UpdateEntreprisePermission]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer


class EntrepriseDetail(generics.RetrieveUpdateDestroyAPIView, UpdateEntreprisePermission):
    # permission_classes = [IsAuthenticated, UpdateEntreprisePermission]
    #permission_classes = [UpdateEntreprisePermission]
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer


def Delete(request, pk):
    user = get_object_or_404(Entreprise, pk=pk)
    if user:
        user.delete()
        return JsonResponse({"status": "ok"}, status=status.HTTP_200_OK)
    return JsonResponse({"status": "not found"}, status=status.HTTP_400_BAD_REQUEST)


def Update(request,  pk):
    serializer = Entreprise(data=request.data)
    serializer.is_valid(raise_exception=True)
    obj, created = Entreprise.objects.update_or_create(
        pk=pk,
        defaults=serializer.validated_data)
    return Response()


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
