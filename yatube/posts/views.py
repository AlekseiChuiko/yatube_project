from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
    
# Главная страница
def index(request): 
    return HttpResponse('Главная страница')

# Страница  постов
def group_posts(request, slug):
    return HttpResponse('Страница  постов, отфильтрованные по группам')