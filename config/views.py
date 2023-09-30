from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse('Hello, world!')


def hello_world_2(request):
    a = '<h1>Hello, world!</h1>'
    return HttpResponse(a)


def render_page(request):
    return render(request, './index_1.html')


def render_page_2(request):
    b = '<h1>Hello, world!</h1>'
    text = 'Новый текст'
    return render (request, './index_2.html', {
        'b': b,  # сначала идет ключ, который прописан в шаблоне, а потом переменная из тела функции
        'text': text
    })
