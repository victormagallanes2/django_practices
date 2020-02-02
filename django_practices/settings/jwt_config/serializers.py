from rest_framework.serializers import ModelSerializer
from django_practices.usercustom.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')