from django.urls import path
from tour.views import tour_list_view

urlpatterns = [
    path('tours/', tour_list_view, name='tour_list'),
]