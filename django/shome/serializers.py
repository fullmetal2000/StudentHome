from shome.models import UniversityInfo
from rest_framework import serializers

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = ('name', 'url', 'introduction', 'ranking',
        	      'studentnum', 'fee', 'image', 'apartment',
        	      'food', 'housing', 'car', 'translink',
        	      'shopping', 'tourist', 'sports', 'googlemaps')

