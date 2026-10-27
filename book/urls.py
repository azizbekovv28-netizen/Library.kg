from django.urls import path
from book.views import about_me, my_favorite_writer, sayings_of_great_poets

urlpatterns = [
    path('about_me/', about_me, name='about_me'),
    path('my_favorite_writer/', my_favorite_writer, name='my_favorite_writer'),
    path('sayings_of_great_poets/', sayings_of_great_poets, name='sayings_of_great_poets'),
]