from django.contrib import admin
from tour.models import Tour, Person, CategoryTour, BookingTour, CommentTour

admin.site.register(Tour)
admin.site.register(Person)
admin.site.register(CategoryTour)
admin.site.register(BookingTour)
admin.site.register(CommentTour)

# Register your models here.
