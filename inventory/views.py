from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, TemplateView, )
from django.contrib.auth.decorators import login_required


import inventory
from inventory.forms import SupplyForm
from inventory.models import WorkStation, Supply


# Create your views here.


# ===========================================
# WS Models
# ===========================================
class WorkStationList(ListView):
    model = WorkStation
    fields = '__all__'


class WorkStationDetail(DetailView):
    model = WorkStation
    fields = '__all__'


class WorkStationCreate(LoginRequiredMixin, CreateView):
    model = WorkStation
    fields = '__all__'
    success_url = reverse_lazy('workstation-list')


class WorkStationUpdate(LoginRequiredMixin, UpdateView):
    model = WorkStation
    fields = '__all__'
    success_url = reverse_lazy('workstation-list')


class WorkStationDelete(LoginRequiredMixin, DeleteView):
    model = WorkStation
    success_url = reverse_lazy('workstation-list')


# ==============================================
# Supply model
# ==============================================
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
        return render(request, "core/404.html")
    context = {'supply': supply}

    return render(request, "inventory/supply_detail.html", context)

@login_required
def create_supply(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplies-list')
    else:
        form = SupplyForm()
    return render(request, 'inventory/create_supply.html', {"form": form})

@login_required
def update_supply(request, slug):
    supply = get_object_or_404(Supply, slug=slug)
    if request.method == 'POST':
        form = SupplyForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            return redirect('supplies-list')
    else:
        form = SupplyForm(instance=supply)
    return render(request, 'inventory/update_supply.html', {"form": form})

@login_required
def delete_supply(request, slug):
    supply = get_object_or_404(Supply, slug=slug)
    if request.method == 'POST':
        supply.delete()
        return redirect('supplies-list')

    return render(request, 'inventory/confirm_delete.html', {"supply": supply})
