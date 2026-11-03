from django.db import models

class CategoryTour(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ManyToManyField(CategoryTour, blank=True)

    def __str__(self):
        return f'{self.title} - ${self.price}'

class BookingTour(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f'Booking for {self.person} - {self.tour.title}'

from django.core.validators import MaxValueValidator, MinValueValidator

class CommentTour(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    
    description = models.TextField(default='Отличный тур!')
    mark = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment by {self.person} on {self.tour.title}'