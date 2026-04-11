from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, )

from inventory.forms import SupplyForm
from inventory.models import WorkStation, Supply


# Create your views here.

def index(request):
    return render(request, 'inventory/index.html')

class WorkStationList(ListView):
    model = WorkStation
    fields = '__all__'


class WorkStationDetail(DetailView):
    model = WorkStation
    fields = '__all__'


class WorkStationCreate(CreateView):
    model = WorkStation
    fields = '__all__'


class WorkStationUpdate(UpdateView):
    model = WorkStation
    fields = '__all__'


class WorkStationDelete(DeleteView):
    model = WorkStation
    success_url = reverse_lazy('workstation-list')


def list_supplies(request):
    supplies_query = Supply.objects.all()
    queried_supply = request.GET.get('q')
    if queried_supply is not None:
        supplies_query = supplies_query.filter(name__icontains=queried_supply)
    context = {'supply_list': supplies_query}

    return render(request, "inventory/supplies_list.html", context)


def supply_detail(request, slug):
    try:
        supply = Supply.objects.get(slug=slug)
    except Supply.DoesNotExist:
        return render(request, "error_404.html")
    context = {'supply': supply}

    return render(request, "inventory/supply_detail.html", context)


def create_supply(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-supplies')
    else:
        form = SupplyForm()
    return render(request, 'inventory/create_supply.html', {"form": form})


def update_supply(request, slug):
    supply = get_object_or_404(Supply, slug=slug)
    if request.method == 'POST':
        form = SupplyForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('list-supplies')
    else:
        form = SupplyForm(instance=supply)
    return render(request, 'inventory/update_supply.html', {"form": form})


def delete_supply(request, slug):
    supply = get_object_or_404(Supply, slug=slug)
    if request.method == 'POST':
        supply.delete()
        return redirect('list-supplies')
    return redirect('list-supplies')
