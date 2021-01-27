from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import RequestContext

from .forms import SignUpForm, LoginForm

from django.db import models
from IT_items.models import Motherboard, PowerSupply, PC, VideoCard, LanCard, SoundCard


def main(request):
    pcs = PC.objects.all()

    #####################
    motherboards = Motherboard.objects.all()

    labels_motherboard_brand = []
    data_motherboard_brand = []
    motherboard_dict = dict()
    queryset_motherboard = Motherboard.objects.order_by('brand')[:]

    for qs in queryset_motherboard:
        if qs.brand not in motherboard_dict:
            motherboard_dict[qs.brand] = 1
            labels_motherboard_brand.append(qs.brand)
        else:
            motherboard_dict[qs.brand] += 1

    for key in motherboard_dict.keys():
        data_motherboard_brand.append(motherboard_dict[key])

    print(motherboard_dict)
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

    print(motherboard_dict)
    motherboard_dict = dict()

    #####################

    power_supplies = PowerSupply.objects.all()
    video_cards = VideoCard.objects.all()
    lan_cards = LanCard.objects.all()
    sound_cards = SoundCard.objects.all()

    power_supplies_count = power_supplies.count()

    return render(request, 'main/main.html', {'motherboards': motherboards,
                                              'labels_motherboard_brand': labels_motherboard_brand,
                                              'data_motherboard_brand': data_motherboard_brand,
                                              'labels_motherboard_form_factor': labels_motherboard_form_factor,
                                              'data_motherboard_form_factor': data_motherboard_form_factor,
                                              'pcs': pcs,
                                              'power_supplies': power_supplies,
                                              'power_supplies_count': power_supplies_count,
                                              'video_cards': video_cards,
                                              'lan_cards': lan_cards,
                                              'sound_cards': sound_cards})


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
