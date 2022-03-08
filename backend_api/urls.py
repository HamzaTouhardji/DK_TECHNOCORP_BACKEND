from rest_framework import routers
from django.urls import path, include
from .views import EntrepriseList, EntrepriseDetail, Delete, Update
from rest_framework import renderers
from . import views

app_name = 'backend_api'

router = routers.DefaultRouter()
router.register(r'', EntrepriseList, basename='listEntrepriseCreated')


urlpatterns = [
    path('<int:pk>', EntrepriseDetail.as_view(),
         name='detailEntrepriseCreated'),
    path('delete/<int:pk>', Delete,
         name='detailEntrepriseCreated'),
    path('update/<int:pk>', Update,
         name='detailEntrepriseCreated'),
    #path('', EntrepriseList.as_view(), name='listEntrepriseCreated'),
    path('', include(router.urls)),
]
