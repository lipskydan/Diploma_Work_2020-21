from django import forms

from django.forms import widgets

from .models import Motherboard, PC


class AddPcForm(forms.ModelForm):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True,
                                       error_messages={'unique':'Персональний комп\'ютор з таким інвентарним номером вже існує.'})
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
                                                required=True, help_text='Обов’язково, у разі відсутності - вказати що відсутньо',
                                                localize=True)

    motherboard_brand = forms.CharField(label='Бренд материнської плати', max_length=30,
                                        required=True, help_text='Обов’язково, у разі відсутності - вказати що відсутньо')

    motherboard_model = forms.CharField(label='Модель материнської плати', max_length=30,
                                        required=True, help_text='Обов’язково, у разі відсутності - вказати що відсутньо',
                                        localize=True)

    motherboard_integrated_graphics = forms.BooleanField(label='Інтегрована відеокарта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class':'checkbox'}))

    motherboard_integrated_sound_card = forms.BooleanField(label='Інтегрована звукова-карта', localize=True,
                                                           required=False, help_text='Вказати чи наявна',
                                                           widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
    motherboard_integrated_lan_card = forms.BooleanField(label='Інтегрована мережева-карта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class':'checkbox'}))

    class Meta:
        model = Motherboard
        fields = ['motherboard_serial_number', 'motherboard_brand', 'motherboard_model',
                  'motherboard_integrated_graphics', 'motherboard_integrated_sound_card', 'motherboard_integrated_lan_card']
