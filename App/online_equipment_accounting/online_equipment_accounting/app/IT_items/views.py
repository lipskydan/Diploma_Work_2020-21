from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from django.urls import reverse
from django.views.generic import View

from .models import PC, Motherboard
from .forms import AddPcForm, AddMotherboardForm


def IT_items(request):
    items_pc = PC.objects.all()
    # items_motherboard = Motherboard.object.all()
    return render(request, 'IT_items/IT-items.html', {'items_pc': items_pc})


def pc_accessories(request):
    items_motherboard = Motherboard.object.all()
    return render(request, 'IT_items/pc_accessories.html', {'items_motherboard': items_motherboard})


def item_detail(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_detail')

    return render(request, 'IT_items/IT_item_detail.html', {'item': item})


def pc_accessories_detail(request, item_name, item_id):
    item = None
    try:
        if item_name == 'Motherboard':
            item = Motherboard.object.get(id=item_id)
    except:
        raise Http404('ERROR pc_accessories_detail')

    return render(request, 'IT_items/pc_accessories_detail.html', {'item': item})


def add_item(request):
    return render(request, 'IT_items/add_item.html')


def add_pc(request):

    if request.method == 'POST':
        form = AddPcForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # motherboard = Motherboard(model=cd['motherboard_model'], serial_number=cd['motherboard_serial_number'])
            # motherboard.save()
            item = PC(inventory_number=cd['inventory_number'], floor=cd['floor'], room=cd['room'], motherboard=cd['motherboard'])
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
    else:
        form = AddPcForm()
        pass

    return render(request, 'IT_items/add_pc.html', {'form': form})


def add_motherboard(request):
    if request.method == 'POST':
        form = AddMotherboardForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            motherboard = Motherboard(model=cd['motherboard_model'], serial_number=cd['motherboard_serial_number'])
            motherboard.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddMotherboardForm()
        pass

    return render(request, 'IT_items/add_motherboard.html', {'form': form})


def item_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_delete')

    # if item.motherboard:
    #     item.motherboard.delete()

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:IT_items'))


def pc_accessories_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'Motherboard':
            item = Motherboard.object.get(id=item_id)
    except:
        raise Http404('ERROR pc_accessories_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def item_update(request, item_name, item_id):
    item = None

    if item_name == 'PC':
        item = PC.objects.get(id=item_id)

    if request.method == 'POST':
        form = AddPcForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            item.inventory_number = request.POST['inventory_number']
            item.floor = request.POST['floor']
            item.room = request.POST['room']
            item.motherboard = cd['motherboard']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
        except:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        form = AddPcForm()
        return render(request, 'IT_items/IT_item_update.html', {'item': item, 'form': form})


def pc_accessories_update(request, item_name, item_id):
    item = None

    if item_name == 'Motherboard':
        item = Motherboard.object.get(id=item_id)

    if request.method == 'POST':
        item.model = request.POST['motherboard_model']
        item.serial_number = request.POST['motherboard_serial_number']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/pc_accessories_update.html', {'item': item})


