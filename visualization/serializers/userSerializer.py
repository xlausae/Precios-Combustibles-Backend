from rest_framework                              import serializers
from visualization.models.user                   import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email']
        
    def create(self, validated_data):
        usuario  = User.objects.create(**validated_data)
        return usuario

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'name'    : user.name,
            'email'   : user.email,
        }