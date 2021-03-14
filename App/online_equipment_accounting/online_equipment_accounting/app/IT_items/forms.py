from django import forms

from django.forms import widgets

from .models import PC, Motherboard, PowerSupply, VideoCard, LanCard, SoundCard

from .models import MOTHERBOARD_FROM_FACTORS, TYPE_RAM_SLOTS, TYPE_OPTICAL_DRIVE, TYPE_CONNECTOR_OF_OPTICAL_DRIVE


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

    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all(), label='Материнська плата',
                                         empty_label='', required=False, help_text='Необов’язково',
                                         localize=True,
                                         widget=widgets.Select(attrs={'size': 1}))

    power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок живлення',
                                          empty_label='', required=False, help_text='Необов’язково',
                                          localize=True,
                                          widget=widgets.Select(attrs={'size': 1}))

    video_card = forms.ModelChoiceField(queryset=VideoCard.objects.all(), label='Відео карта',
                                        empty_label='', required=False, help_text='Необов’язково',
                                        localize=True,
                                        widget=widgets.Select(attrs={'size': 1}))

    lan_card = forms.ModelChoiceField(queryset=LanCard.objects.all(), label='Мережева плата',
                                      empty_label='', required=False, help_text='Необов’язково',
                                      localize=True,
                                      widget=widgets.Select(attrs={'size': 1}))

    # sound_card = forms.ModelChoiceField(queryset=SoundCard.objects.all(), label='Звукова плата',
    #                                     empty_label='', required=False, help_text='Необов’язково',
    #                                     localize=True,
    #                                     widget=widgets.Select(attrs={'size': 1}))

    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'place', 'motherboard', 'power_supply']

        widgets = {
            'motherboard': forms.Select(attrs={'class': 'form-control'}),
            'power_supply': forms.Select(attrs={'class': 'form-control'})
        }


class AddMotherboardForm(forms.ModelForm):
    motherboard_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                                required=True, localize=True,
                                                help_text='Обов’язково',
                                                error_messages={
                                                    'unique': 'Материнська плата з таким серійним номером вже існує.'},
                                                widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    motherboard_brand = forms.CharField(label='Бренд', max_length=30,
                                        required=True,
                                        help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                        widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    motherboard_model = forms.CharField(label='Модель', max_length=30,
                                        required=True,
                                        help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                        localize=True,
                                        widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    motherboard_form_factor = forms.ChoiceField(label='Форм-фактор', choices=MOTHERBOARD_FROM_FACTORS,
                                                required=False, localize=True, help_text='Необов’язково',
                                                widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    motherboard_type_ram_slot = forms.ChoiceField(label='Тип слоту для ОЗУ', choices=TYPE_RAM_SLOTS,
                                                  required=False, localize=True, help_text='Необов’язково',
                                                  widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

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
                  'motherboard_integrated_lan_card', 'motherboard_form_factor']


class AddPowerSupplyForm(forms.ModelForm):
    power_supply_brand = forms.CharField(label='Бренд', max_length=30, required=True,
                                         help_text='Обов’язково, у разі відсутності - вказати відсутньо')

    power_supply_model = forms.CharField(label='Модель', max_length=30, required=True, localize=True,
                                         help_text='Обов’язково, у разі відсутності - вказати відсутньо')

    power_supply_serial_number_or_inventory_number = forms.CharField(label='Серійний/Інвентарний номер', max_length=30,
                                                                     required=True, localize=True,
                                                                     help_text='Обов’язково')

    power_supply_power_consumption = forms.IntegerField(label='Максимальна споживана потужність від мережі',
                                                        required=True,
                                                        help_text='Обов’язково',
                                                        localize=True)

    class Meta:
        model = PowerSupply
        fields = ['power_supply_brand', 'power_supply_model', 'power_supply_serial_number_or_inventory_number',
                  'power_supply_power_consumption']


class AddVideoCard(forms.ModelForm):
    video_card_brand = forms.CharField(label='Бренд', max_length=30, required=False,
                                       help_text='Необов’язково')

    video_card_model = forms.CharField(label='Модель', max_length=30, required=False, localize=True,
                                       help_text='Необов’язково')

    video_card_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                               required=True, localize=True,
                                               help_text='Обов’язково')

    video_card_memory_size = forms.IntegerField(label='Обсяг пам\'яті', localize=True, required=True,
                                                help_text='Обов’язково, вказувати в MB (1 GB = 1024 MB)')

    class Meta:
        model = VideoCard
        fields = ['video_card_brand', 'video_card_model', 'video_card_serial_number', 'video_card_memory_size']


class AddLanCard(forms.ModelForm):
    lan_card_brand = forms.CharField(label='Бренд', max_length=30, required=False,
                                     help_text='Необов’язково')

    lan_card_model = forms.CharField(label='Модель', max_length=30, required=False, localize=True,
                                     help_text='Необов’язково')

    lan_card_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                             required=True, localize=True,
                                             help_text='Обов’язково')

    class Meta:
        model = LanCard
        fields = ['lan_card_brand', 'lan_card_model', 'lan_card_serial_number']


class AddSoundCard(forms.ModelForm):
    sound_card_brand = forms.CharField(label='Бренд', max_length=30, required=False,
                                       help_text='Необов’язково')

    sound_card_model = forms.CharField(label='Модель', max_length=30, required=False, localize=True,
                                       help_text='Необов’язково')

    sound_card_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                               required=True, localize=True,
                                               help_text='Обов’язково')

    class Meta:
        model = SoundCard
        fields = ['sound_card_brand', 'sound_card_model', 'sound_card_serial_number']


class AddOpticalDrive(forms.ModelForm):
    optical_drive_brand = forms.CharField(label='Бренд', max_length=30, required=False,
                                          help_text='Необов’язково')

    optical_drive_model = forms.CharField(label='Модель', max_length=30, required=False, localize=True,
                                          help_text='Необов’язково')

    optical_drive_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                                  required=True, localize=True,
                                                  help_text='Обов’язково')

    optical_drive_type_drive = forms.ChoiceField(label='Тип оптичного накопичувача', choices=TYPE_OPTICAL_DRIVE,
                                                 required=False, localize=True, help_text='Необов’язково',
                                                 widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    optical_drive_type_connector = forms.ChoiceField(label='Тип роз\'єму',
                                                     choices=TYPE_CONNECTOR_OF_OPTICAL_DRIVE,
                                                     required=False, localize=True, help_text='Необов’язково',
                                                     widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = SoundCard
        fields = ['optical_drive_brand', 'optical_drive_model', 'optical_drive_serial_number',
                  'optical_drive_type_drive', 'optical_drive_type_connector']
