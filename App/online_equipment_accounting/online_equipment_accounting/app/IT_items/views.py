from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import PC
from .forms import AddPcForm


def IT_items(request):
    items = PC.objects.all()
    return render(request, 'IT_items/IT-items.html', {'items': items})


def item_detail(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_detail')

    return render(request, 'IT_items/item_detail.html', {'item': item})


def add_item(request):
    return render(request, 'IT_items/add_item.html')


def add_pc(request):
    if request.method == 'POST':
        form = AddPcForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            item = PC(inventory_number=cd['inventory_number'], floor=cd['floor'], room=cd['room'])
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
    else:
        form = AddPcForm()

    return render(request, 'IT_items/add_pc.html', {'form': form})

def add_switch(request):
    if request.method == 'POST':

        # item = PC(inventory_number=request.POST['inventory_number'], floor=request.POST['floor'], room=request.POST['room'])
        # item.save()
        return HttpResponseRedirect(reverse('IT_items:IT_items'))
    else:
        return render(request, 'IT_items/add_pc.html')


def item_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:IT_items'))


def item_update(request, item_name, item_id):
    item = None

    if item_name == 'PC':
        item = PC.objects.get(id=item_id)

    if request.method == 'POST':
        item.name = item.name
        item.inventory_number = request.POST['inventory_number']
        item.floor = request.POST['floor']
        item.room = request.POST['room']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
        except:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/post_update.html', {'item': item})





