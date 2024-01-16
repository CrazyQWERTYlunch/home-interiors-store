from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request): #  в request Попадают данные о запросе и пользователе
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home'
    }
    return render(request, 'main/index.html', context=context)


def about(request) -> HttpResponse: #  в request Попадают данные о запросе и пользователе
    return HttpResponse('About us')
