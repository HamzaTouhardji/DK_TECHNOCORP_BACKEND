from rest_framework import serializers
from backend.models import Entreprise


class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'founder', 'content', 'status')
        #fields = '__all__'
        model = Entreprise
