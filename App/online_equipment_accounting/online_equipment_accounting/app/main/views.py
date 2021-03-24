from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import RequestContext

from .forms import SignUpForm, LoginForm

from django.db import models
from IT_items.models import Motherboard, PowerSupply, PC, VideoCard, LanCard, SoundCard, OpticalDrive


def get_motherboard_brand_data_and_labels():
    motherboard_dict = dict()
    queryset_motherboard = Motherboard.objects.order_by('brand')[:]
    labels_motherboard_brand = []
    data_motherboard_brand = []

    for qs in queryset_motherboard:
        if qs.brand not in motherboard_dict:
            motherboard_dict[qs.brand] = 1
            labels_motherboard_brand.append(qs.brand)
        else:
            motherboard_dict[qs.brand] += 1

    for key in motherboard_dict.keys():
        data_motherboard_brand.append(motherboard_dict[key])

    return data_motherboard_brand, labels_motherboard_brand


def get_motherboard_form_factor_data_and_labels():
    motherboard_dict = dict()
    queryset_motherboard = Motherboard.objects.order_by('form_factor')[:]
    labels_motherboard_form_factor = []
    data_motherboard_form_factor = []

    for qs in queryset_motherboard:
        if qs.form_factor not in motherboard_dict:
            motherboard_dict[qs.form_factor] = 1
            labels_motherboard_form_factor.append(qs.form_factor)
        else:
            motherboard_dict[qs.form_factor] += 1

    for key in motherboard_dict.keys():
        data_motherboard_form_factor.append(motherboard_dict[key])

    return data_motherboard_form_factor, labels_motherboard_form_factor


def get_motherboard_integrated_items_data_and_labels():
    data_motherboard_integrated_graphics = Motherboard.objects.filter(integrated_graphics=True).count()
    data_motherboard_integrated_sound_card = Motherboard.objects.filter(integrated_sound_card=True).count()
    data_motherboard_integrated_lan_card = Motherboard.objects.filter(integrated_lan_card=True).count()
    motherboards_count = Motherboard.objects.all().count()

    data_motherboard = [data_motherboard_integrated_graphics, data_motherboard_integrated_sound_card,
                        data_motherboard_integrated_lan_card, motherboards_count]

    labels_motherboard = ['інтегрована відеокарта',
                          'інтегрована звукова-карта',
                          'інтегрована мережева-карта',
                          'загальна кількість']

    return data_motherboard, labels_motherboard


def get_motherboard_ram_data_and_labels():
    motherboard_dict = dict()
    queryset_motherboard = Motherboard.objects.order_by('form_factor')[:]
    labels_motherboard_ram = []
    data_motherboard_ram = []

    for qs in queryset_motherboard:
        if qs.type_ram_slot not in motherboard_dict:
            motherboard_dict[qs.type_ram_slot] = 1
            labels_motherboard_ram.append(qs.type_ram_slot)
        else:
            motherboard_dict[qs.type_ram_slot] += 1

    for key in motherboard_dict.keys():
        data_motherboard_ram.append(motherboard_dict[key])

    return data_motherboard_ram, labels_motherboard_ram


def get_power_supply_consumption_data_and_labels():
    power_supply_dict = dict()
    queryset_power_supply = PowerSupply.objects.order_by('power_consumption')[:]
    labels_power_supply = []
    data_power_supply = []

    for qs in queryset_power_supply:
        if qs.power_consumption not in power_supply_dict:
            power_supply_dict[qs.power_consumption] = 1
            labels_power_supply.append(str(str(qs.power_consumption) + ' Вт'))
        else:
            power_supply_dict[qs.power_consumption] += 1

    for key in power_supply_dict.keys():
        data_power_supply.append(power_supply_dict[key])

    return data_power_supply, labels_power_supply


def get_power_supply_brand_data_and_labels():
    power_supply_dict = dict()
    queryset_power_supply = PowerSupply.objects.order_by('brand')[:]
    labels_power_supply = []
    data_power_supply = []

    for qs in queryset_power_supply:
        if qs.brand not in power_supply_dict:
            power_supply_dict[qs.brand] = 1
            labels_power_supply.append(qs.brand)
        else:
            power_supply_dict[qs.brand] += 1

    for key in power_supply_dict.keys():
        data_power_supply.append(power_supply_dict[key])

    return data_power_supply, labels_power_supply


def get_lan_card_brand_data_and_labels():
    lan_card_dict = dict()
    queryset_lan_card = LanCard.objects.order_by('brand')[:]
    labels_lan_card = []
    data_lan_card = []

    for qs in queryset_lan_card:
        if qs.brand not in lan_card_dict:
            lan_card_dict[qs.brand] = 1
            labels_lan_card.append(qs.brand)
        else:
            lan_card_dict[qs.brand] += 1

    for key in lan_card_dict.keys():
        data_lan_card.append(lan_card_dict[key])

    return data_lan_card, labels_lan_card


def get_sound_card_brand_data_and_labels():
    sound_card_dict = dict()
    queryset_sound_card = SoundCard.objects.order_by('brand')[:]
    labels_sound_card = []
    data_sound_card = []

    for qs in queryset_sound_card:
        if qs.brand not in sound_card_dict:
            sound_card_dict[qs.brand] = 1
            labels_sound_card.append(qs.brand)
        else:
            sound_card_dict[qs.brand] += 1

    for key in sound_card_dict.keys():
        data_sound_card.append(sound_card_dict[key])

    return data_sound_card, labels_sound_card


def get_optical_drive_brand_data_and_labels():
    optical_drive_dict = dict()
    queryset_optical_drive = OpticalDrive.objects.order_by('brand')[:]
    labels_optical_drive = []
    data_optical_drive = []

    for qs in queryset_optical_drive:
        if qs.brand not in optical_drive_dict:
            optical_drive_dict[qs.brand] = 1
            labels_optical_drive.append(qs.brand)
        else:
            optical_drive_dict[qs.brand] += 1

    for key in optical_drive_dict.keys():
        data_optical_drive.append(optical_drive_dict[key])

    return data_optical_drive, labels_optical_drive


def get_optical_drive_type_drive_data_and_labels():
    optical_drive_dict = dict()
    queryset_optical_drive = OpticalDrive.objects.order_by('type_drive')[:]
    labels_optical_drive = []
    data_optical_drive = []

    for qs in queryset_optical_drive:
        if qs.type_drive not in optical_drive_dict:
            optical_drive_dict[qs.type_drive] = 1
            labels_optical_drive.append(qs.type_drive)
        else:
            optical_drive_dict[qs.type_drive] += 1

    for key in optical_drive_dict.keys():
        data_optical_drive.append(optical_drive_dict[key])

    return data_optical_drive, labels_optical_drive


def get_optical_drive_type_connector_data_and_labels():
    optical_drive_dict = dict()
    queryset_optical_drive = OpticalDrive.objects.order_by('type_connector')[:]
    labels_optical_drive = []
    data_optical_drive = []

    for qs in queryset_optical_drive:
        if qs.type_connector not in optical_drive_dict:
            optical_drive_dict[qs.type_connector] = 1
            labels_optical_drive.append(qs.type_connector)
        else:
            optical_drive_dict[qs.type_connector] += 1

    for key in optical_drive_dict.keys():
        data_optical_drive.append(optical_drive_dict[key])

    return data_optical_drive, labels_optical_drive


def get_video_card_brand_data_and_labels():
    dict_item = dict()
    queryset = VideoCard.objects.order_by('brand')[:]
    labels = []
    data = []

    for qs in queryset:
        if qs.brand not in dict_item:
            dict_item[qs.brand] = 1
            labels.append(qs.brand)
        else:
            dict_item[qs.brand] += 1

    for key in dict_item.keys():
        data.append(dict_item[key])

    return data, labels


def get_video_card_memory_size_data_and_labels():
    dict_item = dict()
    queryset = VideoCard.objects.order_by('memory_size')[:]
    labels = []
    data = []

    for qs in queryset:
        if qs.memory_size not in dict_item:
            dict_item[qs.memory_size] = 1
            labels.append([str(str(qs.memory_size) + ' MB'), str('( ' + str(round(qs.memory_size/1024)) + ' GB )')])
        else:
            dict_item[qs.memory_size] += 1

    for key in dict_item.keys():
        data.append(dict_item[key])

    return data, labels


def main(request):
    pcs = PC.objects.all()
    motherboards = Motherboard.objects.all()
    power_supplies = PowerSupply.objects.all()
    optical_drives = OpticalDrive.objects.all()
    video_cards = VideoCard.objects.all()
    lan_cards = LanCard.objects.all()
    sound_cards = SoundCard.objects.all()

    data_motherboard_brand, labels_motherboard_brand = get_motherboard_brand_data_and_labels()
    data_motherboard_form_factor, labels_motherboard_form_factor = get_motherboard_form_factor_data_and_labels()
    data_motherboard_integrated_items, labels_motherboard_integrated_items = get_motherboard_integrated_items_data_and_labels()
    data_motherboard_ram, labels_motherboard_ram = get_motherboard_ram_data_and_labels()

    data_power_supply_consumption, labels_power_supply_consumption = get_power_supply_consumption_data_and_labels()
    data_power_supply_brand, labels_power_supply_brand = get_power_supply_brand_data_and_labels()

    data_lan_card_brand, labels_lan_card_brand = get_lan_card_brand_data_and_labels()

    data_sound_card_brand, labels_sound_card_brand = get_sound_card_brand_data_and_labels()

    data_optical_drive_brand, labels_optical_drive_brand = get_optical_drive_brand_data_and_labels()
    data_optical_drive_type, labels_optical_drive_type = get_optical_drive_type_drive_data_and_labels()
    data_optical_drive_type_connector, labels_optical_drive_type_connector = get_optical_drive_type_connector_data_and_labels()

    data_video_card_brand, labels_video_card_brand = get_video_card_brand_data_and_labels()
    data_video_card_memory_size, labels_video_card_memory_size = get_video_card_memory_size_data_and_labels()

    power_supplies_count = power_supplies.count()

    return render(request, 'main/main.html', {'motherboards': motherboards,

                                              'labels_motherboard_brand': labels_motherboard_brand,
                                              'data_motherboard_brand': data_motherboard_brand,
                                              'labels_motherboard_form_factor': labels_motherboard_form_factor,
                                              'data_motherboard_form_factor': data_motherboard_form_factor,
                                              'labels_motherboard_integrated_items': labels_motherboard_integrated_items,
                                              'data_motherboard_integrated_items': data_motherboard_integrated_items,
                                              'labels_motherboard_ram': labels_motherboard_ram,
                                              'data_motherboard_ram': data_motherboard_ram,

                                              'pcs': pcs,

                                              'power_supplies': power_supplies,

                                              'labels_power_supply_consumption': labels_power_supply_consumption,
                                              'data_power_supply_consumption': data_power_supply_consumption,
                                              'labels_power_supply_brand': labels_power_supply_brand,
                                              'data_power_supply_brand': data_power_supply_brand,

                                              'optical_drives': optical_drives,

                                              'labels_optical_drive_brand': labels_optical_drive_brand,
                                              'data_optical_drive_brand': data_optical_drive_brand,
                                              'labels_optical_drive_type': labels_optical_drive_type,
                                              'data_optical_drive_type': data_optical_drive_type,
                                              'labels_optical_drive_type_connector': labels_optical_drive_type_connector,
                                              'data_optical_drive_type_connector': data_optical_drive_type_connector,

                                              'video_cards': video_cards,

                                              'labels_video_card_brand': labels_video_card_brand,
                                              'data_video_card_brand': data_video_card_brand,
                                              'labels_video_card_memory_size': labels_video_card_memory_size,
                                              'data_video_card_memory_size': data_video_card_memory_size,

                                              'lan_cards': lan_cards,

                                              'labels_lan_card_brand': labels_lan_card_brand,
                                              'data_lan_card_brand': data_lan_card_brand,

                                              'sound_cards': sound_cards,

                                              'labels_sound_card_brand': labels_sound_card_brand,
                                              'data_sound_card_brand': data_sound_card_brand,

                                              'power_supplies_count': power_supplies_count})


def user_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'main/login_invalid.html')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    user_logout(request)
