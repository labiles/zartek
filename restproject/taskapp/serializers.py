from .models import Rides
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self, validated_data):
        user=get_user_model().objects.create(
             username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')

class Taskserializers(serializers.ModelSerializer):
    class Meta:
        model=Rides
        fields=['id','rider','driver','pickup_location','dropoff_location','status','created_at','updated_at']