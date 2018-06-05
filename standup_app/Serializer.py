#author raniniveda
from rest_framework import serializers
from .models import UserProfile
#import django.contrib.auth.password_validation as validators

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            user = UserProfile.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                mobile_number=validated_data['mobile_number'],
                password=validated_data['password']
            )
            user.set_password(validated_data['password'])
            print (user.password)
            user.save()

            return user

    def validate_password(self,validated_data):
            #user=UserProfile(**validated_data)
            print validated_data,dir(validated_data),type(validated_data)
            password=str(validated_data)

            if len(password)<8:
                raise serializers.ValidationError("Min length of password should be 8 characters")
            return super(UserSerializer, self).validate_password(validated_data)
            
    class Meta:
        model = UserProfile
        fields = ('email', 'username','mobile_number','password')
        write_only_fields=('password',)