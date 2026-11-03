from django.shortcuts import render
from tour.models import Tour    

def tour_list_view(request):
    if request.method == "GET":
        tour = Tour.objects.all().order_by('-id')
    return render(request, 'tours_list.html', {'tour': tour})

# Create your views here.
