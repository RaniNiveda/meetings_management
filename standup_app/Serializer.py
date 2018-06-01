#author raniniveda
from rest_framework import serializers
from .models import UserProfile

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
    class Meta:
        model = UserProfile
        fields = ('email', 'username','mobile_number','password')
        write_only_fields=('password',)