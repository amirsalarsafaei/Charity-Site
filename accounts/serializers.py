from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'address', 'gender', 'age', 'description',
                  'first_name', 'last_name', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            description=validated_data['description']
        )
        user.save()
        return user
