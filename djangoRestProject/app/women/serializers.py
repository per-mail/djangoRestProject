from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenSerializer наследуется от класса ModelSerializer из serializers.
class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
# указываем, что используем модель Women
        model = Women
# указываем, что используем все поля из модели
        fields = "__all__"

