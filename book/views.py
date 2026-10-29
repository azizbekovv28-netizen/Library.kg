from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from book.models import Book

def book_list_view(request):
    if request.method == 'GET':
        book = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'book': book})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'blog_id': book_id})

def about_me(request):
    if request.method == 'GET':
        return HttpResponse ('<p>Привет, меня зовут Азим, мне 22 лет.</p>'
        '<p>Я учусь в Geeks_ed на backand разработчика.</p> ' \
        '<p>Я люблю программирование и спорт.</p> '
        '<p>Я занимаюсь тяжёлой атлетикой и боксом.</p>')

def my_favorite_writer(request):
    if request.method == 'GET':
        return HttpResponse ('<p>Мой любимые писатели:</p>' \
        '<p>1. Чынгыз Айтматов</p>' \
        '<p>2. Агата Кристи</p>' \
        '<p>3. Лев Толстой</p>')

def sayings_of_great_poets(request):
    if request.method == 'GET':
        return HttpResponse ("<p>«Перед каждым человеком стоит неизбывная задача — быть человеком, сегодня, завтра, всегда»</p> <img src='https://www.trtavaz.com.tr/uploads/photos/2022/06/10/9da5d980b07f462c98bcbf9f30e37e26.png?w=640'>" \
        "<p>«Ложь открывает тому, кто умеет слушать, не меньше, чем правда», «докопаться до истины никогда не поздно», а «осторожность — лучшее оружие».</p> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFiOwhmt2NJ1r6H7cPDauxX3Oj91uzbl-OlqG8rekt4w&s=10'>"
        "<p>«Прошедшее было, будущего нет, есть только одно настоящее»</p> <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqIP1kQHh8wXX80kfZnHXloKumZ_Zzn2CSHKAqrXbZ6w&s=10'>")
# Create your views here.
