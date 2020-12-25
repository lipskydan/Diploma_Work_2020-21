from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import PC


def items(request):
    items = PC.objects.all()
    return render(request, 'items/items.html', {'items': items})


def item_detail(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_detail')

    return render(request, 'items/item_detail.html', {'item': item})


def add_item(request):
    return render(request, 'items/add_item.html')


def add_pc(request):
    if request.method == 'POST':
        item = PC(inventory_number=request.POST['inventory_number'], floor=request.POST['floor'], room=request.POST['room'])
        item.save()
        return HttpResponseRedirect(reverse('items:items'))
    else:
        return render(request, 'items/add_pc.html')


def item_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_delete')

    item.delete()

    return HttpResponseRedirect(reverse('items:items'))


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
            return HttpResponseRedirect(reverse('items:items'))
        except:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'items/post_update.html', {'item': item})





