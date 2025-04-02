
from rest_framework import serializers
from .models import Applications


class ApplicationsSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Applications
        
        fields = '__all__'
        
        read_only_fields = ['applicant','status']
        
        