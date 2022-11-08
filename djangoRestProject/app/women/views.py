from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer

# делаем пагинацию
# создаём отдельный класс пагинации наследуем класс WomenAPIListPagination от PageNumberPagination
class WomenAPIListPagination(PageNumberPagination):
    page_size = 3 # количество записей на странице
    page_size_query_param = 'page_size' # с помощью этого параметра клиент может изменять количество записей на странице
    max_page_size = 2 # ограничение для page_size_query_param не более 2

#WomenAPIList наследуется от класса ListCreateAPIView
class WomenAPIList(generics.ListCreateAPIView):
    #queryset возвращает данные клиенту, он получает список записей возвращающихся клиенту
    #queryset связываем с моделью Women
    queryset = Women.objects.all()
    #serializer_clas - это сериаллайзер который будет применяться к queryset из строки выше
    #ему присваиваем наш сериаллайзер WomenSerializer
    serializer_class = WomenSerializer
    #настройка доступа к редактированию записей
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # подключаем класс пагинации к Women
    pagination_class = WomenAPIListPagination

#редактирование записей
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # настройка доступа к редактированию записей
    permission_classes = (IsAuthenticated, )
# пример подключения способа аутентификации только по токенам
    # authentication_classes = (TokenAuthentication, )

 # удаление записей
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # настройка доступа к удалению записей
    permission_classes = (IsAdminOrReadOnly, )
