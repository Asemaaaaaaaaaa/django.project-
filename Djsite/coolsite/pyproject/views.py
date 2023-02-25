from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from.models import *


menu = ["Тренинги", "Психология", "Саморазвития", "Мастер-классы"]
def index(request):

    return render(request, 'pyproject/index.html',{ 'title': 'Главная страница'})

def training1(request):
    t1 = Training1.objects.all()
    return render(request, 'pyproject/training1.html', {'t1': t1})

def training2(request):
    t2 = Training2.objects.all()
    return render(request, 'pyproject/training2.html', {'t2': t2})


def books(request):
    b = Books.objects.all()
    categories = Category.objects.all()
    return render(request,'pyproject/books.html',{'b': b ,'categories': categories , 'category_selected':0 })

    def show_category(request, category_id):
        b = Books.objects.filter(category_id=category_id)
        categories = Category.objects.all()
        return render(request, 'pyproject/books.html',
                      {'b': b, 'categories': categories, 'category_selected': category_id})

    return HttpResponse(f"<h1>Страница категория</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')