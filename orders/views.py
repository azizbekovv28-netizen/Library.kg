from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Orders
from orders.forms import OrdersForm

def create_abit_view(request):
    if request.method == 'POST':
      form_abit = OrdersForm(request.POST, request.FILES)
      if form_abit.is_valid():
            form_abit.save()
            return redirect('/abit_list/')
    else:
        form_abit = OrdersForm()
    
    return render(request, 'create_list.html', {'form': form_abit})

def abit_list_view(request):
    if request.method == 'GET':
        abit_list = Orders.objects.all().order_by('-id')
    return render(request, 'abit_list.html', {'abits': abit_list})

def update_abit_view(request, id):
    abit_id = get_object_or_404(Orders, id=id)
    if request.method == 'POST':
        form_abit = OrdersForm(request.POST, request.FILES, instance=abit_id)
        if form_abit.is_valid():
            form_abit.save()
            return redirect('order_list')
    else:
        form_abit = OrdersForm(instance=abit_id)
    return render(request, 'abit_update.html', {'form': form_abit})

def delete_abit_view(request, id):
    abit_id = get_object_or_404(Orders, id=id)
    abit_id.delete()
    return redirect('/abit_list/')
