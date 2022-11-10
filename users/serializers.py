from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        model = User
        fields = "__all__"
            
        def create(self, validated_data):
            user = super().create(validated_data)
            password = user.password
            user.set_password(password)
            user.save()
            return user

        def update(self, validated_data):
            user = super().create(validated_data)
            password = user.password
            user.set_password(password)
            user.save()
            return user 

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email # name 대신 email 써준다. token['email’] = user.email
        token['token_message'] = "sparta_time_attack"
        

        return token
