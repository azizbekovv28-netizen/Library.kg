from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='укажите название книги')
    description = models.TextField(blank=True, verbose_name= 'укажите описание книги')
    image = models.ImageField(upload_to='book/', verbose_name='загрузите фото')
    GENRE_BOOK = (
        ('Фэнтези', 'Фэнтези'),
        ('Детектив', 'Детектив'),
        ('Романтика', 'Романтика'),
        ('Приключения', 'Приключения'),
        ('Ужасы', 'Ужасы'),
        ('Триллер', 'Триллер'),
        ('Драма', 'Драма'),
        ('Историческая литература', 'Историческая литература'),
        ('Классическая литература', 'Классическая литература'),
        ('Научная литература', 'Научная литература'),
        ('Научная фантастика', 'Научная фантастика'),
        ('Психология', 'Психология'),
        ('Саморазвитие', 'Саморазвитие'),
        ('Бизнес и финансы', 'Бизнес и финансы'),

    )
    genre_book = models.CharField(max_length=100, choices=GENRE_BOOK, verbose_name='укажите жанр')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
