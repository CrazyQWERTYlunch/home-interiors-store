from django.shortcuts import render
from django.shortcuts import HttpResponse

from goods.models import Categories

# Create your views here.
def index(request): #  в request Попадают данные о запросе и пользователе
    
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', context=context)


def about(request): #  в request Попадают данные о запросе и пользователе
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему это классный магазин'
    }
    return render(request, 'main/about.html', context=context)
