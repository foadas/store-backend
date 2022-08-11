from djoser.serializers import UserCreateSerializer as base
from djoser.serializers import UserSerializer


class UserCreateSerializer(base):

    class Meta(base.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class CurrentUserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'username']
