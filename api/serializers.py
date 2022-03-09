from dataclasses import field
from statistics import mode
from rest_framework import serializers

from app1.models import visit
from app1.models import testing
from app1.models import mr_user
from app1.models import dr_user



class mr_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = mr_user
        # fields = ['name', 'rollno']
        fields= "__all__"

class dr_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = dr_user
        # fields = ['name', 'rollno']
        fields= "__all__"

class visitSerializer(serializers.ModelSerializer):
    class Meta:
        model = visit
        # fields = ['name', 'rollno']
        fields= "__all__"

class testingSerializer(serializers.ModelSerializer):
    class Meta:
        model = testing
        # fields = ['name', 'rollno']
        fields= "__all__"


class mrloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = mr_user
        fields = ['user_name', 'first_name', 'last_name']

        
