from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, \
    HttpResponseBadRequest
from django.shortcuts import render, redirect

from .models import *
# Create your views here.
def index(request):
    return render(request,'pyproject/index.html')

def training1(request):
    t1 = Training1.objects.all()
    return render(request,'pyproject/training1.html',{'t1':t1})
def training_manager1(request):
    tr1 = Training_manager1.objects.all()
    return render(request,'pyproject/training_manager1.html',{'tr1':tr1})
def training2(request):
    t2 = Training2.objects.all()
    return render(request,'pyproject/training2.html',{'t2':t2})
def books(request):
    b = Books.objects.all()
    categories = Category.objects.all()
    return render(request,'pyproject/books.html',{'b':b,'categories': categories ,'category_selected':0 })

def show_category(request,category_id):
    b=Books.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'pyproject/books.html', {'b': b, 'categories': categories, 'category_selected': category_id})


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')


def forbidden(request,exception):
    return HttpResponseForbidden('<h1>Доступ запрещен </h1>')


def serverError(exception):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')


def badRequest(request,exception):
    return HttpResponseBadRequest('<h1>Неверный запрос </h1>')

def show_post(request, post_id):
     return HttpResponse(f"Отображение статьи с id = {post_id}")


class BookAPIView(APIView):
    def get(self,request):
        b = Books.objects.all()
        return Response({'books': BookSerializer(b, many=True).data})

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})
    def put(self,request,*args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not allowed"})

        try:
            instance = Books.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post" : serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            book = Books.objects.get(pk=pk)

        except:
            return Response({"error": "Object does not exists"})
        book.delete()
        return Response({"post": "deleted post " })

class Training1APIView(generics.ListAPIView):
    queryset = Training1.objects.all()
    serializer_class = Training1Serializer

class Training2APIView(generics.ListAPIView):
    queryset = Training2.objects.all()
    serializer_class = Training1Serializer

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')