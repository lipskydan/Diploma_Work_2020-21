from django import forms

from django.forms import widgets

from .models import PC, Motherboard, PowerSupply


class UpdatePcForm(forms.ModelForm):
    motherboard = forms.ModelChoiceField(queryset=Motherboard.object.all(), label='Материнська плата',
                                         empty_label='Відсутня', required=False, help_text='Необов’язково',
                                         localize=True,
                                         widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок живлення',
                                          empty_label='Відсутній', required=False, help_text='Необов’язково',
                                          localize=True,
                                          widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'place', 'motherboard', 'power_supply']


class AddPcForm(forms.ModelForm):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True,
                                       error_messages={
                                           'unique': 'Персональний комп\'ютор з таким інвентарним номером вже існує.'})
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

    power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок живлення',
                                          empty_label='', required=False, help_text='Необов’язково',
                                          localize=True,
                                          widget=widgets.Select(attrs={'size': 1}))

    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'place', 'motherboard', 'power_supply']

        widgets = {
            'motherboard': forms.Select(attrs={'class': 'form-control'}),
            'power_supply': forms.Select(attrs={'class': 'form-control'})
        }


class AddMotherboardForm(forms.ModelForm):
    motherboard_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                                required=True,
                                                help_text='Обов’язково, у разі відсутності - вказати що відсутньо',
                                                localize=True)

    motherboard_brand = forms.CharField(label='Бренд', max_length=30,
                                        required=True,
                                        help_text='Обов’язково, у разі відсутності - вказати відсутньо')

    motherboard_model = forms.CharField(label='Модель', max_length=30,
                                        required=True,
                                        help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                        localize=True)

    motherboard_integrated_graphics = forms.BooleanField(label='Інтегрована відеокарта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    motherboard_integrated_sound_card = forms.BooleanField(label='Інтегрована звукова-карта', localize=True,
                                                           required=False, help_text='Вказати чи наявна',
                                                           widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    motherboard_integrated_lan_card = forms.BooleanField(label='Інтегрована мережева-карта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    class Meta:
        model = Motherboard
        fields = ['motherboard_serial_number', 'motherboard_brand', 'motherboard_model',
                  'motherboard_integrated_graphics', 'motherboard_integrated_sound_card',
                  'motherboard_integrated_lan_card']


class AddPowerSupplyForm(forms.ModelForm):
    power_supply_brand = forms.CharField(label='Бренд', max_length=30, required=True,
                                         help_text='Обов’язково, у разі відсутності - вказати відсутньо')

    power_supply_model = forms.CharField(label='Модель', max_length=30, required=True, localize=True,
                                         help_text='Обов’язково, у разі відсутності - вказати відсутньо')

    power_supply_serial_number_or_inventory_number = forms.CharField(label='Серійний/Інвентарний номер', max_length=30,
                                                                     required=True, localize=True,
                                                                     help_text='Обов’язково')

    power_supply_power_consumption = forms.IntegerField(label='Максимальна споживана потужність від мережі',
                                                        required=False,
                                                        help_text="Необов’язково (одиниця вимірювання вати)",
                                                        localize=True)

    class Meta:
        model = PowerSupply
        fields = ['power_supply_brand', 'power_supply_model', 'power_supply_serial_number_or_inventory_number',
                  'power_supply_power_consumption']
