from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from typing import Dict

from .forms import AddPcForm, AddMotherboardForm, AddPowerSupplyForm, AddVideoCard, AddLanCard, AddSoundCard, \
    AddOpticalDrive, AddSolidStateDriveForm, AddHardDiskDriveForm

from .models import MOTHERBOARD_FROM_FACTORS, TYPE_RAM_SLOTS, TYPE_OPTICAL_DRIVE, TYPE_CONNECTOR_OF_OPTICAL_DRIVE, \
    TYPE_OPERATING_SYSTEM, TYPE_CENTRAL_PROCESSING_UNIT
from .models import PC, Motherboard, PowerSupply, VideoCard, LanCard, SoundCard, OpticalDrive, SolidStateDrive, \
    HardDiskDrive
from .utils import render_to_pdf

import pdfkit


def check_denied_access_add(func):
    def wrapper(request):
        if not request.user.groups.filter(name__in=['Редактор']).exists():
            return render(request, 'IT_items/denied_access.html')
        else:
            return func(request)

    return wrapper


def check_denied_access_del_or_update(func):
    def wrapper(request, item_name, item_id):
        if not request.user.groups.filter(name__in=['Редактор']).exists():
            return render(request, 'IT_items/denied_access.html')
        else:
            return func(request, item_name, item_id)

    return wrapper


def IT_items(request):
    items_pc = PC.objects.all()
    return render(request, 'IT_items/IT-items.html', {'items_pc': items_pc})


def pc_accessories(request):
    items_motherboard = Motherboard.objects.all()
    items_power_supply = PowerSupply.objects.all()
    items_video_card = VideoCard.objects.all()
    items_lan_cards = LanCard.objects.all()
    items_sound_cards = SoundCard.objects.all()
    items_optical_drive = OpticalDrive.objects.all()
    items_solid_state_drive = SolidStateDrive.objects.all()
    items_hard_disk_drive = HardDiskDrive.objects.all()

    return render(request, 'IT_items/pc_accessories.html', {'items_motherboard': items_motherboard,
                                                            'items_power_supply': items_power_supply,
                                                            'items_video_card': items_video_card,
                                                            'items_lan_cards': items_lan_cards,
                                                            'items_sound_cards': items_sound_cards,
                                                            'items_optical_drive': items_optical_drive,
                                                            'items_solid_state_drive': items_solid_state_drive,
                                                            'items_hard_disk_drive': items_hard_disk_drive})


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
        if item_name == 'OpticalDrive':
            item = OpticalDrive.objects.get(id=item_id)
        if item_name == 'SolidStateDrive':
            item = SolidStateDrive.objects.get(id=item_id)
        if item_name == 'HardDiskDrive':
            item = HardDiskDrive.objects.get(id=item_id)
    except:
        raise Http404('ERROR pc_accessories_detail')

    return render(request, 'IT_items/pc_accessories_detail.html', {'item': item})


@check_denied_access_add
def add(request):
    return render(request, 'IT_items/add.html')


# def add_item(request):
#     return render(request, 'IT_items/add.html')


@check_denied_access_add
def add_pc(request):
    if request.method == 'POST':
        form = AddPcForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            item = PC(inventory_number=cd['inventory_number'], floor=cd['floor'], room=cd['room'], place=cd['place'],
                      operating_system=cd['operating_system'], text_field=cd['text_field'],
                      motherboard=cd['motherboard'],
                      solid_state_drive=cd['solid_state_drive'],
                      hard_disk_drive=cd['hard_disk_drive'],
                      power_supply=cd['power_supply'],
                      video_card=cd['video_card'],
                      lan_card=cd['lan_card'],
                      sound_card=cd['sound_card'],
                      optical_drive=cd['optical_drive'])

            item.save()

            return HttpResponseRedirect(reverse('IT_items:IT_items'))
    else:
        form = AddPcForm()
        pass

    return render(request, 'IT_items/add_pc.html', {'form': form})


@check_denied_access_add
def add_motherboard(request):
    if request.method == 'POST':
        form = AddMotherboardForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            motherboard = Motherboard(serial_number=cd['motherboard_serial_number'],
                                      brand=cd['motherboard_brand'],
                                      model=cd['motherboard_model'],
                                      central_processing_unit=cd['motherboard_central_processing_unit'],
                                      integrated_graphics=cd['motherboard_integrated_graphics'],
                                      integrated_sound_card=cd['motherboard_integrated_sound_card'],
                                      integrated_lan_card=cd['motherboard_integrated_lan_card'],
                                      form_factor=cd['motherboard_form_factor'],
                                      type_ram_slot=cd['motherboard_type_ram_slot'])

            # motherboard.save()
            try:
                motherboard.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': motherboard.serial_number,
                                                               'name_of_item': motherboard.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddMotherboardForm()
        pass

    return render(request, 'IT_items/add_motherboard.html', {'form': form})


@check_denied_access_add
def add_solid_state_drive(request):
    if request.method == 'POST':
        form = AddSolidStateDriveForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            solid_state_drive = SolidStateDrive(serial_number=cd['solid_state_drive_serial_number'],
                                                brand=cd['solid_state_drive_brand'],
                                                model=cd['solid_state_drive_model'],
                                                memory_size=cd['solid_state_drive_memory_size'])

            try:
                solid_state_drive.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': solid_state_drive.serial_number,
                                                               'name_of_item': solid_state_drive.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddSolidStateDriveForm()
        pass

    return render(request, 'IT_items/add_solid_state_drive.html', {'form': form})


@check_denied_access_add
def add_hard_disk_drive(request):
    if request.method == 'POST':
        form = AddHardDiskDriveForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            hard_disk_drive = HardDiskDrive(serial_number=cd['hard_disk_drive_serial_number'],
                                            brand=cd['hard_disk_drive_brand'],
                                            model=cd['hard_disk_drive_model'],
                                            memory_size=cd['hard_disk_drive_memory_size'])

            try:
                hard_disk_drive.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': hard_disk_drive.serial_number,
                                                               'name_of_item': hard_disk_drive.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddHardDiskDriveForm()
        pass

    return render(request, 'IT_items/add_hard_disk_drive.html', {'form': form})


@check_denied_access_add
def add_power_supply(request):
    if request.method == 'POST':
        form = AddPowerSupplyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            power_supply = PowerSupply(brand=cd['power_supply_brand'], model=cd['power_supply_model'],
                                       serial_or_inventory_number=cd['power_supply_serial_number_or_inventory_number'],
                                       power_consumption=cd['power_supply_power_consumption'])
            # power_supply.save()
            try:
                power_supply.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': power_supply.serial_or_inventory_number,
                                                               'name_of_item': power_supply.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddPowerSupplyForm()
        pass

    return render(request, 'IT_items/add_power_supply.html', {'form': form})


@check_denied_access_add
def add_video_card(request):
    if request.method == 'POST':
        form = AddVideoCard(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            video_card = VideoCard(brand=cd['video_card_brand'],
                                   model=cd['video_card_model'],
                                   serial_number=cd['video_card_serial_number'],
                                   memory_size=cd['video_card_memory_size'])
            # video_card.save()
            try:
                video_card.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': video_card.serial_number,
                                                               'name_of_item': video_card.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddVideoCard()
        pass

    return render(request, 'IT_items/add_video_card.html', {'form': form})


@check_denied_access_add
def add_lan_card(request):
    if request.method == 'POST':
        form = AddLanCard(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            lan_card = LanCard(brand=cd['lan_card_brand'],
                               model=cd['lan_card_model'],
                               serial_number=cd['lan_card_serial_number'])
            # lan_card.save()
            try:
                lan_card.save()
            except:
                return render(request, 'IT_items/error.html', {'serial_number': lan_card.serial_number,
                                                               'name_of_item': lan_card.name})

            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddLanCard()
        pass

    return render(request, 'IT_items/add_lan_card.html', {'form': form})


@check_denied_access_add
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


@check_denied_access_add
def add_optical_drive(request):
    if request.method == 'POST':
        form = AddOpticalDrive(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            optical_drive = OpticalDrive(brand=cd['optical_drive_brand'],
                                         model=cd['optical_drive_model'],
                                         serial_number=cd['optical_drive_serial_number'],
                                         type_drive=cd['optical_drive_type_drive'],
                                         type_connector=cd['optical_drive_type_connector'])
            optical_drive.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
    else:
        form = AddOpticalDrive()
        pass

    return render(request, 'IT_items/add_optical_drive.html', {'form': form})


@check_denied_access_del_or_update
def item_delete(request, item_name, item_id):
    item = None
    try:
        if item_name == 'PC':
            item = PC.objects.get(id=item_id)
    except:
        raise Http404('ERROR item_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:IT_items'))


@check_denied_access_del_or_update
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
        elif item_name == 'OpticalDrive':
            item = OpticalDrive.objects.get(id=item_id)
        elif item_name == 'SolidStateDrive':
            item = SolidStateDrive.objects.get(id=item_id)
        elif item_name == 'HardDiskDrive':
            item = HardDiskDrive.objects.get(id=item_id)
    except:
        raise Http404('ERROR pc_accessories_delete')

    item.delete()

    return HttpResponseRedirect(reverse('IT_items:pc_accessories'))


@check_denied_access_del_or_update
def pc_update(request, item_name, item_id):
    item = None
    operating_systems = None
    motherboards = None
    solid_state_drives = None
    hard_disk_drives = None
    power_supplies = None
    video_cards = None
    lan_cards = None
    sound_cards = None
    optical_drives = None

    if item_name == 'PC':
        item = PC.objects.get(id=item_id)

        motherboards = Motherboard.objects.filter()
        solid_state_drives = SolidStateDrive.objects.filter()
        hard_disk_drives = HardDiskDrive.objects.filter()
        power_supplies = PowerSupply.objects.filter()
        video_cards = VideoCard.objects.filter()
        lan_cards = LanCard.objects.filter()
        sound_cards = SoundCard.objects.filter()
        optical_drives = OpticalDrive.objects.filter()

        operating_systems = [el[0] for el in TYPE_OPERATING_SYSTEM]

    if request.method == 'POST':

        item.inventory_number = request.POST['inventory_number']
        item.floor = request.POST['floor']
        item.room = request.POST['room']
        item.place = request.POST['place']
        item.operating_system = request.POST.get('operating_system', None)
        item.text_field = request.POST.get('text_field', False)

        motherboard = request.POST.get('motherboard', None)
        if motherboard != 'None':
            motherboard_dic = motherboard.split()
            motherboard = Motherboard.objects.get(model=motherboard_dic[2],
                                                  brand=motherboard_dic[1],
                                                  serial_number=motherboard_dic[5])
            item.motherboard = motherboard
        else:
            item.motherboard = None

        solid_state_drive = request.POST.get('solid_state_drive', None)
        if solid_state_drive != 'None':
            solid_state_drive_dic = solid_state_drive.split()
            solid_state_drive = SolidStateDrive.objects.get(brand=solid_state_drive_dic[0],
                                                            serial_number=solid_state_drive_dic[2])
            item.solid_state_drive = solid_state_drive
        else:
            item.solid_state_drive = None

        hard_disk_drive = request.POST.get('hard_disk_drive', None)
        if hard_disk_drive != 'None':
            hard_disk_drive_dic = hard_disk_drive.split()
            hard_disk_drive = HardDiskDrive.objects.get(brand=hard_disk_drive_dic[0],
                                                        serial_number=hard_disk_drive_dic[2])
            item.hard_disk_drive = hard_disk_drive
        else:
            item.hard_disk_drive = None

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

        sound_card = request.POST.get('sound_card', None)
        if sound_card != 'None':
            sound_card_dic = sound_card.split()
            sound_card = SoundCard.objects.get(model=sound_card_dic[2],
                                               brand=sound_card_dic[1],
                                               serial_number=sound_card_dic[5])
            item.sound_card = sound_card
        else:
            item.sound_card = None

        optical_drive = request.POST.get('optical_drive', None)
        # optical_drive = item.optical_drive
        # print(optical_drive)

        if optical_drive != 'None':
            optical_drive_dic = optical_drive.split()
            optical_drive = OpticalDrive.objects.get(model=optical_drive_dic[2],
                                                     brand=optical_drive_dic[1],
                                                     serial_number=optical_drive_dic[5])
            item.optical_drive = optical_drive
        else:
            item.optical_drive = None

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:IT_items'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/pc_update.html', {'item': item,
                                                           'operating_systems': operating_systems,
                                                           'motherboards': motherboards,
                                                           'solid_state_drives': solid_state_drives,
                                                           'hard_disk_drives': hard_disk_drives,
                                                           'power_supplies': power_supplies,
                                                           'video_cards': video_cards,
                                                           'lan_cards': lan_cards,
                                                           'sound_cards': sound_cards,
                                                           'optical_drives': optical_drives})


@check_denied_access_del_or_update
def motherboard_update(request, item_name, item_id):
    item = None
    form_factors = None
    type_ram_slots = None
    central_processing_units = None

    if item_name == 'Motherboard':
        item = Motherboard.objects.get(id=item_id)

        form_factors = [el[0] for el in MOTHERBOARD_FROM_FACTORS]
        type_ram_slots = [el[0] for el in TYPE_RAM_SLOTS]
        central_processing_units = [el[0] for el in TYPE_CENTRAL_PROCESSING_UNIT]

    if request.method == 'POST':

        if item_name == 'Motherboard':
            item.brand = request.POST['motherboard_brand']
            item.model = request.POST['motherboard_model']

            item.serial_number = request.POST['motherboard_serial_number']

            item.central_processing_unit = request.POST.get('motherboard_central_processing_unit', None)
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
                                                                    'type_ram_slots': type_ram_slots,
                                                                    'central_processing_units': central_processing_units})


@check_denied_access_del_or_update
def solid_state_drive_update(request, item_name, item_id):
    item = None

    if item_name == 'SolidStateDrive':
        item = SolidStateDrive.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'SolidStateDrive':
            item.brand = request.POST['solid_state_drive_brand']
            item.model = request.POST['solid_state_drive_model']
            item.serial_number = request.POST['solid_state_drive_serial_number']
            item.memory_size = request.POST['solid_state_drive_memory_size']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/solid_state_drive_update.html', {'item': item})


@check_denied_access_del_or_update
def hard_disk_drive_update(request, item_name, item_id):
    item = None

    if item_name == 'HardDiskDrive':
        item = HardDiskDrive.objects.get(id=item_id)

    if request.method == 'POST':

        if item_name == 'HardDiskDrive':
            item.brand = request.POST['hard_disk_drive_brand']
            item.model = request.POST['hard_disk_drive_drive_model']
            item.serial_number = request.POST['hard_disk_drive_serial_number']
            item.memory_size = request.POST['hard_disk_drive_memory_size']

        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/hard_disk_drive_update.html', {'item': item})


@check_denied_access_del_or_update
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


@check_denied_access_del_or_update
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


@check_denied_access_del_or_update
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


@check_denied_access_del_or_update
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


@check_denied_access_del_or_update
def optical_drive_update(request, item_name, item_id):
    item = None
    type_drives = None
    type_connectors = None

    if item_name == 'OpticalDrive':
        item = OpticalDrive.objects.get(id=item_id)

        type_drives = [el[0] for el in TYPE_OPTICAL_DRIVE]
        type_connectors = [el[0] for el in TYPE_CONNECTOR_OF_OPTICAL_DRIVE]

    if request.method == 'POST':

        if item_name == 'OpticalDrive':
            item.brand = request.POST['optical_drive_brand']
            item.model = request.POST['optical_drive_model']
            item.serial_number = request.POST['optical_drive_serial_number']

            item.type_drive = request.POST.get('optical_drive_type_drive', None)
            item.type_connector = request.POST.get('optical_drive_type_connector', None)
        try:
            item.save()
            return HttpResponseRedirect(reverse('IT_items:pc_accessories'))
        except ObjectDoesNotExist:
            return 'При обновлении оборудывания произошла ошибка'

    else:
        return render(request, 'IT_items/optical_drive_update.html', {'item': item,
                                                                      'type_drives': type_drives,
                                                                      'type_connectors': type_connectors})


def error(request):
    return render(request, 'IT_items/error.html')


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

        from datetime import datetime

        context = {
            'user_first_name': request.user.first_name,
            'user_last_name': request.user.last_name,

            'current_time': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            'item_id': item.id,
            'item_name': item.name,
            'item_name_for_user': item.name_for_user,
            'item_inventory_number': item.inventory_number,

            'item_floor': item.floor,
            'item_room': item.room,
            'item_place': item.place,

            'item_operating_system': item.operating_system,
            'item_text_field': item.text_field,

            'item_motherboard_brand': item.motherboard.brand if item.motherboard else None,
            'item_motherboard_model': item.motherboard.model if item.motherboard else None,
            'item_motherboard_serial_number': item.motherboard.serial_number if item.motherboard else None,
            'item_motherboard_form_factor': item.motherboard.form_factor if item.motherboard else None,
            'item_motherboard_type_ram_slot': item.motherboard.type_ram_slot if item.motherboard else None,
            'item_motherboard_central_processing_unit': item.motherboard.central_processing_unit if item.motherboard else None,
            'item_motherboard_integrated_graphics': item.motherboard.integrated_graphics if item.motherboard else None,
            'item_motherboard_integrated_sound_card': item.motherboard.integrated_sound_card if item.motherboard else None,
            'item_motherboard_integrated_lan_card': item.motherboard.integrated_lan_card if item.motherboard else None,

            'item_solid_state_drive_brand': item.solid_state_drive.brand if item.solid_state_drive else None,
            'item_solid_state_drive_model': item.solid_state_drive.model if item.solid_state_drive else None,
            'item_solid_state_drive_serial_number': item.solid_state_drive.serial_number if item.solid_state_drive else None,
            'item_solid_state_drive_memory_size': item.solid_state_drive.memory_size if item.solid_state_drive else None,

            'item_hard_disk_drive_brand': item.hard_disk_drive.brand if item.hard_disk_drive else None,
            'item_hard_disk_drive_model': item.hard_disk_drive.model if item.hard_disk_drive else None,
            'item_hard_disk_drive_serial_number': item.hard_disk_drive.serial_number if item.hard_disk_drive else None,
            'item_hard_disk_drive_memory_size': item.hard_disk_drive.memory_size if item.hard_disk_drive else None,

            'item_power_supply_brand': item.power_supply.brand if item.power_supply else None,
            'item_power_supply_model': item.power_supply.model if item.power_supply else None,
            'item_power_supply_serial_number': item.power_supply.serial_or_inventory_number if item.power_supply else None,
            'item_power_supply_power_consumption': item.power_supply.power_consumption if item.power_supply else None,

            'item_video_card_brand': item.video_card.brand if item.video_card else None,
            'item_video_card_model': item.video_card.model if item.video_card else None,
            'item_video_card_serial_number': item.video_card.serial_number if item.video_card else None,
            'item_video_card_memory_size': item.video_card.memory_size if item.video_card else None,

            'item_lan_card_brand': item.lan_card.brand if item.lan_card else None,
            'item_lan_card_model': item.lan_card.model if item.lan_card else None,
            'item_lan_card_serial_number': item.lan_card.serial_number if item.lan_card else None,

            'item_sound_card_brand': item.sound_card.brand if item.sound_card else None,
            'item_sound_card_model': item.sound_card.model if item.sound_card else None,
            'item_sound_card_serial_number': item.sound_card.serial_number if item.sound_card else None,

            'item_optical_drive_brand': item.optical_drive.brand if item.optical_drive else None,
            'item_optical_drive_model': item.optical_drive.model if item.optical_drive else None,
            'item_optical_drive_serial_number': item.optical_drive.serial_number if item.optical_drive else None,
            'item_optical_drive_type_drive': item.optical_drive.type_drive if item.optical_drive else None,
            'item_optical_drive_type_connector': item.optical_drive.type_connector if item.optical_drive else None,
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
