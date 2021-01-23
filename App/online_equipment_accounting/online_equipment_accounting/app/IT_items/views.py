from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import AddPcForm, AddMotherboardForm, AddPowerSupplyForm, AddVideoCard, AddLanCard, AddSoundCard
from .models import MOTHERBOARD_FROM_FACTORS, TYPE_RAM_SLOTS
from .models import PC, Motherboard, PowerSupply, VideoCard, LanCard, SoundCard
from .utils import render_to_pdf


def IT_items(request):
    items_pc = PC.objects.all()
    return render(request, 'IT_items/IT-items.html', {'items_pc': items_pc})


def pc_accessories(request):
    items_motherboard = Motherboard.objects.all()
    items_power_supply = PowerSupply.objects.all()
    items_video_card = VideoCard.objects.all()
    items_lan_cards = LanCard.objects.all()
    items_sound_cards = SoundCard.objects.all()

    return render(request, 'IT_items/pc_accessories.html', {'items_motherboard': items_motherboard,
                                                            'items_power_supply': items_power_supply,
                                                            'items_video_card': items_video_card,
                                                            'items_lan_cards': items_lan_cards,
                                                            'items_sound_cards': items_sound_cards})


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
            item = Motherboard.objects.get(id=item_id)
        if item_name == 'PowerSupply':
            item = PowerSupply.objects.get(id=item_id)
        if item_name == 'VideoCard':
            item = VideoCard.objects.get(id=item_id)
        if item_name == 'LanCard':
            item = LanCard.objects.get(id=item_id)
        if item_name == 'SoundCard':
            item = SoundCard.objects.get(id=item_id)
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

            item = PC(inventory_number=cd['inventory_number'], floor=cd['floor'], room=cd['room'], place=cd['place'],
                      motherboard=cd['motherboard'],
                      power_supply=cd['power_supply'],
                      video_card=cd['video_card'],
                      lan_card=cd['lan_card'])

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
            motherboard = Motherboard(brand=cd['motherboard_brand'],
                                      model=cd['motherboard_model'],
                                      serial_number=cd['motherboard_serial_number'],
                                      integrated_graphics=cd['motherboard_integrated_graphics'],
                                      integrated_sound_card=cd['motherboard_integrated_sound_card'],
                                      integrated_lan_card=cd['motherboard_integrated_lan_card'],
                                      form_factor=cd['motherboard_form_factor'],
                                      type_ram_slot=cd['motherboard_type_ram_slot'])
            motherboard.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddMotherboardForm()
        pass

    return render(request, 'IT_items/add_motherboard.html', {'form': form})


def add_power_supply(request):
    if request.method == 'POST':
        form = AddPowerSupplyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            power_supply = PowerSupply(brand=cd['power_supply_brand'], model=cd['power_supply_model'],
                                       serial_or_inventory_number=cd['power_supply_serial_number_or_inventory_number'],
                                       power_consumption=cd['power_supply_power_consumption'])
            power_supply.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddPowerSupplyForm()
        pass

    return render(request, 'IT_items/add_power_supply.html', {'form': form})


def add_video_card(request):
    if request.method == 'POST':
        form = AddVideoCard(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            video_card = VideoCard(brand=cd['video_card_brand'],
                                   model=cd['video_card_model'],
                                   serial_number=cd['video_card_serial_number'],
                                   memory_size=cd['video_card_memory_size'])
            video_card.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddVideoCard()
        pass

    return render(request, 'IT_items/add_video_card.html', {'form': form})


def add_lan_card(request):
    if request.method == 'POST':
        form = AddLanCard(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            lan_card = LanCard(brand=cd['lan_card_brand'],
                               model=cd['lan_card_model'],
                               serial_number=cd['lan_card_serial_number'])
            lan_card.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddLanCard()
        pass

    return render(request, 'IT_items/add_lan_card.html', {'form': form})


def add_sound_card(request):
    if request.method == 'POST':
        form = AddSoundCard(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sound_card = SoundCard(brand=cd['sound_card_brand'],
                                   model=cd['sound_card_model'],
                                   serial_number=cd['sound_card_serial_number'])
            sound_card.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddSoundCard()
        pass

    return render(request, 'IT_items/add_sound_card.html', {'form': form})


def item_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:IT_items'))


def pc_accessories_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'Motherboard':
            item = Motherboard.objects.get(id=item_id)
        elif item_name == 'PowerSupply':
            item = PowerSupply.objects.get(id=item_id)
        elif item_name == 'VideoCard':
            item = VideoCard.objects.get(id=item_id)
        elif item_name == 'LanCard':
            item = LanCard.objects.get(id=item_id)
        elif item_name == 'SoundCard':
            item = SoundCard.objects.get(id=item_id)
    except:
        raise Http404('ERROR pc_accessories_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def motherboard_delete(request, item_name, item_id):
    item = None
    try:
        item = Motherboard.objects.get(id=item_id)
    except:
        raise Http404('ERROR motherboard_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def power_supply_delete(request, item_name, item_id):
    item = None
    try:
        item = PowerSupply.objects.get(name=item_name, id=item_id)
    except:
        raise Http404('ERROR motherboard_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def video_card_delete(request, item_name, item_id):
    item = None
    try:
        item = VideoCard.objects.get(id=item_id)
    except:
        raise Http404('ERROR motherboard_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def lan_card_delete(request, item_name, item_id):
    item = None
    try:
        item = LanCard.objects.get(id=item_id)
    except:
        raise Http404('ERROR motherboard_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def sound_card_delete(request, item_name, item_id):
    item = None
    try:
        item = SoundCard.objects.get(id=item_id)
    except:
        raise Http404('ERROR motherboard_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


def pc_update(request, item_name, item_id):
    item = None
    motherboards = None
    power_supplies = None
    video_cards = None
    lan_cards = None
    sound_cards = None

    if item_name == 'PC':
        item = PC.objects.get(id=item_id)

        motherboards = Motherboard.objects.filter()
        power_supplies = PowerSupply.objects.filter()
        video_cards = VideoCard.objects.filter()
        lan_cards = LanCard.objects.filter()
        sound_cards = SoundCard.objects.filter()

    if request.method == 'POST':

        item.inventory_number = request.POST['inventory_number']
        item.floor = request.POST['floor']
        item.room = request.POST['room']
        item.place = request.POST['place']

        motherboard = request.POST.get('motherboard', None)
        if motherboard != 'None':
            motherboard_dic = motherboard.split()
            motherboard = Motherboard.objects.get(model=motherboard_dic[2],
                                                  brand=motherboard_dic[1],
                                                  serial_number=motherboard_dic[5])
            item.motherboard = motherboard
        else:
            item.motherboard = None

        power_supply = request.POST.get('power_supply', None)
        if power_supply != 'None':
            power_supply_dic = power_supply.split()
            power_supply = PowerSupply.objects.get(model=power_supply_dic[2],
                                                   brand=power_supply_dic[1],
                                                   serial_or_inventory_number=power_supply_dic[5])
            item.power_supply = power_supply
        else:
            item.power_supply = None

        video_card = request.POST.get('video_card', None)
        if video_card != 'None':
            video_card_dic = video_card.split()
            video_card = VideoCard.objects.get(model=video_card_dic[2],
                                               brand=video_card_dic[1],
                                               serial_number=video_card_dic[5])
            item.video_card = video_card
        else:
            item.video_card = None

        lan_card = request.POST.get('lan_card', None)
        if lan_card != 'None':
            lan_card_dic = lan_card.split()
            lan_card = LanCard.objects.get(model=lan_card_dic[2],
                                           brand=lan_card_dic[1],
                                           serial_number=lan_card_dic[5])
            item.lan_card = lan_card
        else:
            item.lan_card = None

        # sound_card = request.POST.get('sound_card', None)
        # if sound_card != 'None':
        #     sound_card_dic = sound_card.split()
        #     sound_card = SoundCard.objects.get(model=sound_card_dic[2],
        #                                        brand=sound_card_dic[1],
        #                                        serial_number=sound_card_dic[5])
        #     item.sound_card = sound_card
        # else:
        #     item.sound_card = None

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/pc_update.html', {'item': item,
                                                           'motherboards': motherboards,
                                                           'power_supplies': power_supplies,
                                                           'video_cards': video_cards,
                                                           'lan_cards': lan_cards})


def motherboard_update(request, item_name, item_id):
    item = None
    form_factors = None
    type_ram_slots = None

    if item_name == 'Motherboard':
        item = Motherboard.objects.get(id=item_id)

        form_factors = [el[0] for el in MOTHERBOARD_FROM_FACTORS]
        type_ram_slots = [el[0] for el in TYPE_RAM_SLOTS]

    if request.method == 'POST':

        if item_name == 'Motherboard':
            item.brand = request.POST['motherboard_brand']
            item.model = request.POST['motherboard_model']

            item.serial_number = request.POST['motherboard_serial_number']

            item.form_factor = request.POST.get('motherboard_form_factor', None)
            item.type_ram_slot = request.POST.get('motherboard_type_ram_slot', None)

            item.integrated_graphics = True if request.POST.get('motherboard_integrated_graphics') else False
            item.integrated_sound_card = True if request.POST.get('motherboard_integrated_sound_card') else False
            item.integrated_lan_card = True if request.POST.get('motherboard_integrated_lan_card') else False

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/motherboard_update.html', {'item': item,
                                                                    'form_factors': form_factors,
                                                                    'type_ram_slots': type_ram_slots})


def power_supply_update(request, item_name, item_id):
    item = None

    if item_name == 'PowerSupply':
        item = PowerSupply.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'PowerSupply':
            item.brand = request.POST['power_supply_brand']
            item.model = request.POST['power_supply_model']
            item.serial_or_inventory_number = request.POST['power_supply_serial_number_or_inventory_number']
            item.power_consumption = request.POST['power_supply_power_consumption']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/power_supply_update.html', {'item': item})


def video_card_update(request, item_name, item_id):
    item = None

    if item_name == 'VideoCard':
        item = VideoCard.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'VideoCard':
            item.brand = request.POST['video_card_brand']
            item.model = request.POST['video_card_model']
            item.serial_number = request.POST['video_card_serial_number']
            item.memory_size = request.POST['video_card_memory_size']
        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/video_card_update.html', {'item': item})


def lan_card_update(request, item_name, item_id):
    item = None

    if item_name == 'LanCard':
        item = LanCard.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'LanCard':
            item.brand = request.POST['lan_card_brand']
            item.model = request.POST['lan_card_model']
            item.serial_number = request.POST['lan_card_serial_number']
        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/lan_card_update.html', {'item': item})


def sound_card_update(request, item_name, item_id):
    item = None

    if item_name == 'SoundCard':
        item = SoundCard.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'SoundCard':
            item.brand = request.POST['sound_card_brand']
            item.model = request.POST['sound_card_model']
            item.serial_number = request.POST['sound_card_serial_number']
        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/sound_card_update.html', {'item': item})


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
