"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *

# from rest_framework import routers
#
# # создаём обьект роутер, обьект класса SimpleRouter
# router = routers.SimpleRouter()
# # регистрируем класс WomenViewSet
# # r - префикс для набора маршрутов
# router.register(r'women', WomenViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
# # весь набор маршрутов связанный с WomenViewSet, который был автоматически сгененрирован роутером
#     path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/ - маршрут для браузера
# авторизация в системе
# rest_framework.urls - из rest_framework подключаем маршруты urls
    path('api/v1/drf-auth/', include('rest_framework.urls')),
# api/v1/drf-auth/
# api/ - означает что api-запрос
# v1/ - версия api
# drf-auth/ - название
# WomenAPIList.as_view() - класс представления из views
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
# подключаем djoser к проекту
    path('api/v1/auth/', include('djoser.urls')), # базовый маршрут для авторизации и других действий связанных с потльзователем
    re_path(r'^auth/', include('djoser.urls.authtoken')),# авторизация по токенам
# подключаем аутентификацию через JWT-токены
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
