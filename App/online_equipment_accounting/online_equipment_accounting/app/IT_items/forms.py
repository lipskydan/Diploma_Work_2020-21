from django import forms

from django.forms import widgets

from .models import Motherboard, PC


class AddPcForm(forms.ModelForm):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True)
    floor = forms.IntegerField(label='Номер поверху', required=True, help_text='Обов’язково',
                               localize=True)
    room = forms.IntegerField(label='Номер кабінету', required=True, help_text='Обов’язково',
                              localize=True)
    place = forms.IntegerField(label='Номер учбового місця', required=False, help_text='Необов’язково',
                               localize=True)

    motherboard = forms.ModelChoiceField(queryset=Motherboard.object.all(), label='Материнська плата',
                                         empty_label='', required=False, help_text='Необов’язково',
                                         localize=True,
                                         widget=widgets.Select(attrs={'size': 1}))

    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'motherboard', ]

        widgets = {
            'motherboard': forms.Select(attrs={'class': 'form-control'})
        }


class AddMotherboardForm(forms.ModelForm):
    motherboard_serial_number = forms.CharField(label='Серійний номер материнської плати', max_length=30,
                                                required=True, help_text='Обов’язково',
                                                localize=True)

    motherboard_model = forms.CharField(label='Модель материнської плати', max_length=30,
                                        required=True, help_text='Обов’язково',
                                        localize=True)

    class Meta:
        model = Motherboard
        fields = ['motherboard_serial_number', 'motherboard_model', ]
