import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from django.urls import reverse
from django.views.generic import View

from .models import PC, Motherboard
from .forms import AddPcForm, AddMotherboardForm

from .utils import render_to_pdf


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

            motherboard = cd['motherboard']
            print('motherboard')
            print(motherboard.model + ' ' + motherboard.serial_number + ' ' + str(motherboard.is_established))

            # motherboard_new = Motherboard.object.get(model=motherboard.model, serial_number=motherboard.serial_number)
            # motherboard_new.is_established = True
            # motherboard_new.save()
            #
            # print('motherboard_new')
            # print(motherboard_new.model + ' ' + motherboard_new.serial_number + ' ' + str(motherboard_new.is_established))

            # motherboard_new = Motherboard.object.get(id=needed_motherboard.id)
            # motherboard_new.is_established = True
            # motherboard_new.save()

            item = PC(inventory_number=cd['inventory_number'], floor=cd['floor'], room=cd['room'], place= cd['place'],
                      motherboard=motherboard_new)
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
            motherboard = Motherboard(brand=cd['motherboard_brand'], model=cd['motherboard_model'], serial_number=cd['motherboard_serial_number'])
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
            item.place = request.POST['place']
            item.motherboard = cd['motherboard']

            # motherboard_new = Motherboard.object.get(model=item.motherboard.model,
            #                                          serial_number=item.motherboard.serial_number)
            #
            # motherboard_new.is_established = False
            #
            # item.motherboard = motherboard_new
            # motherboard_new.save()


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
        item.brand = request.POST['motherboard_brand']
        item.model = request.POST['motherboard_model']
        item.serial_number = request.POST['motherboard_serial_number']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/pc_accessories_update.html', {'item': item})


class GeneratePDF(LoginRequiredMixin, View):

    @staticmethod
    def get(request, item_name, item_id):
        """
        Generate PDF from HTML template
        """
        item = None
        try:
            if item_name == 'PC':
                item = PC.objects.get(id=item_id)
        except:
            raise Http404('ERROR GeneratePdf:get')

        context = {
            'item_id': item.id,
            'item_name': item.name,
            'item_name_for_user': item.name_for_user,
            'item_inventory_number': item.inventory_number,
            'item_floor': item.floor,
            'item_room': item.room,
            'item_motherboard_model': item.motherboard.model,
            'item_motherboard_serial_number': item.motherboard.serial_number,
            'item_place': item.place,
        }

        template = 'IT_items/invoice.html'
        pdf = render_to_pdf(template, context)

        if pdf:
            filename = '{}_#_{}_floor_{}_room_{}.pdf'.format(item.name, item.inventory_number, item.floor, item.room)
            content = 'inline; filename="{}"'.format(filename)

            if request.GET.get('save_to_file') == 'true':
                content = 'attachment; filename="{}"'.format(filename)

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = content
            return response

        return HttpResponse(status=404)