"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from pyproject.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pyproject.urls')),
from django.urls import path,include

from rest_framework import routers

class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get':'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix':'List'}),
        routers.Route(url=r'{prefix}/{lookup}$',
                      mapping={'get':'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix':'Detail'})
    ]
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get':'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix':'List'}),
#         routers.Route(url=r'{prefix}/{lookup}$',
#                       mapping={'get':'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix':'Detail'})
#     ]
router = routers.SimpleRouter()
router.register(r'book',BookViewSet)
# router.register(r'book',BookViewSet)
router.register(r'training1',Training1ViewSet)
router.register(r'training2',Training2ViewSet)
router.register(r'training_manager1',Training_manager1ViewSet)
@@ -47,16 +46,13 @@ class MyCustomRouter(routers.SimpleRouter):
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('',include('project.urls')),
    path('api/v1/',include(router.urls)),#http://127.0.0.1:8000/api/v1/training1/

    path('api/v1/book/',BookAPIList.as_view()),
    path('api/v1/bookcreate/',BookAPICreate.as_view()),
    path('api/v1/book/<int:pk>/',BookAPIUpdate.as_view()),
    path('api/v1/bookdelete/<int:pk>/',BookAPIDestroy.as_view()),

    path('api/v1/',include(router.urls)),#http://127.0.0.1:8000/api/v1/book/

    # path('api/v1/booklist/',BookViewSet.as_view({'get': 'list'})),
    # path('api/v1/booklist/<int:pk>/',BookViewSet.as_view({'put': 'update'})),
    # path('api/v1/bookdetail/<int:pk>/',BookAPIDetailView.as_view()),

    # path('api/v1/training1list/',Training1APIView.as_view()),
    # path('api/v1/training2list/',Training2APIView.as_view())


]
  4
coolsite/project/models.py
@@ -1,7 +1,6 @@
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Training1(models.Model):
    title = models.CharField(max_length=255)
@@ -24,6 +23,7 @@ class Books(models.Model):
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%y/%m/%d/")
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    user = models.ForeignKey(User,verbose_name='Пользователь',on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
]




