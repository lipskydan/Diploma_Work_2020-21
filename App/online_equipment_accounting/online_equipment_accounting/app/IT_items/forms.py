from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from django.forms import widgets

from .models import PC, Motherboard, PowerSupply, VideoCard, LanCard, SoundCard, OpticalDrive, SolidStateDrive, \
    HardDiskDrive, WorkReport

from .models import MOTHERBOARD_FROM_FACTORS, TYPE_RAM_SLOTS, TYPE_OPTICAL_DRIVE, TYPE_CONNECTOR_OF_OPTICAL_DRIVE, \
    TYPE_OPERATING_SYSTEM, TYPE_CENTRAL_PROCESSING_UNIT


class AddPcForm(forms.ModelForm):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True,
                                       error_messages={
                                           'unique': 'Персональний комп\'ютор з таким інвентарним номером вже існує.'},
                                       widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    floor = forms.IntegerField(label='Номер поверху', required=True, help_text='Обов’язково',
                               localize=True, widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
    room = forms.IntegerField(label='Номер кабінету', required=True, help_text='Обов’язково',
                              localize=True, widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
    place = forms.IntegerField(label='Номер учбового місця', required=False, help_text='Необов’язково',
                               localize=True, widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    operating_system = forms.ChoiceField(label='Операційна система', choices=TYPE_OPERATING_SYSTEM,
                                         required=False, localize=True, help_text='Необов’язково',
                                         widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    # text_field = forms.CharField(label='Нотатки', required=False,
    #                              widget=forms.Textarea(attrs={'size': 1, 'class': 'form-control'}))

    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all(), label='Материнська плата',
                                         empty_label='', required=False, help_text='Необов’язково',
                                         localize=True,
                                         widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    solid_state_drive = forms.ModelChoiceField(queryset=SolidStateDrive.objects.all(),
                                               label='Твердотільний накопичувач',
                                               empty_label='', required=False, help_text='Необов’язково',
                                               localize=True,
                                               widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    hard_disk_drive = forms.ModelChoiceField(queryset=HardDiskDrive.objects.all(),
                                             label='Жорсткий магнітний диск',
                                             empty_label='', required=False, help_text='Необов’язково',
                                             localize=True,
                                             widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    power_supply = forms.ModelChoiceField(queryset=PowerSupply.objects.all(), label='Блок живлення',
                                          empty_label='', required=False, help_text='Необов’язково',
                                          localize=True,
                                          widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    video_card = forms.ModelChoiceField(queryset=VideoCard.objects.all(), label='Відео карта',
                                        empty_label='', required=False, help_text='Необов’язково',
                                        localize=True,
                                        widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    lan_card = forms.ModelChoiceField(queryset=LanCard.objects.all(), label='Мережева плата',
                                      empty_label='', required=False, help_text='Необов’язково',
                                      localize=True,
                                      widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    sound_card = forms.ModelChoiceField(queryset=SoundCard.objects.all(), label='Звукова плата',
                                        empty_label='', required=False, help_text='Необов’язково',
                                        localize=True,
                                        widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    optical_drive = forms.ModelChoiceField(queryset=OpticalDrive.objects.all(), label='Оптичний накопичувач',
                                           empty_label='', required=False, help_text='Необов’язково',
                                           localize=True,
                                           widget=widgets.Select(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'place', 'motherboard', 'power_supply',
                  'video_card', 'lan_card', 'sound_card', 'optical_drive']

        widgets = {
            'motherboard': forms.Select(attrs={'class': 'form-control'}),
            'power_supply': forms.Select(attrs={'class': 'form-control'}),
            'video_card': forms.Select(attrs={'class': 'form-control'}),
            'lan_card': forms.Select(attrs={'class': 'form-control'}),
            'sound_card': forms.Select(attrs={'class': 'form-control'}),
            'optical_drive': forms.Select(attrs={'class': 'form-control'}),
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

    motherboard_central_processing_unit = forms.ChoiceField(label='Центральний процесор',
                                                            choices=TYPE_CENTRAL_PROCESSING_UNIT,
                                                            required=False, localize=True, help_text='Необов’язково',
                                                            widget=widgets.Select(
                                                                attrs={'size': 1, 'class': 'form-control'}))

    motherboard_integrated_graphics = forms.BooleanField(label='Інтегрована відеокарта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    motherboard_integrated_sound_card = forms.BooleanField(label='Інтегрована звукова-карта', localize=True,
                                                           required=False, help_text='Вказати чи наявна',
                                                           widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))
    motherboard_integrated_lan_card = forms.BooleanField(label='Інтегрована мережева-карта', localize=True,
                                                         required=False, help_text='Вказати чи наявна',
                                                         widget=forms.CheckboxInput(attrs={'class': 'checkbox'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'motherboard_serial_number',

            Row(
                Column('motherboard_brand', css_class='form-group col-md-6 mb-0'),
                Column('motherboard_model', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            'motherboard_form_factor',
            'motherboard_type_ram_slot',
            'motherboard_central_processing_unit',

            Row(
                Column('motherboard_integrated_graphics', css_class='form-group col-md-4 mb-0'),
                Column('motherboard_integrated_sound_card', css_class='form-group col-md-4 mb-0'),
                Column('motherboard_integrated_lan_card', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Submit('submit', 'Створити')
        )

    class Meta:
        model = Motherboard
        fields = ['motherboard_serial_number', 'motherboard_brand', 'motherboard_model',
                  'motherboard_integrated_graphics', 'motherboard_integrated_sound_card',
                  'motherboard_integrated_lan_card', 'motherboard_form_factor']


class AddSolidStateDriveForm(forms.ModelForm):
    solid_state_drive_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                                      required=True, localize=True,
                                                      help_text='Обов’язково',
                                                      error_messages={
                                                          'unique': 'Твердотільний накопичувач з таким серійним номером вже існує.'},
                                                      widget=widgets.TextInput(
                                                          attrs={'size': 1, 'class': 'form-control'}))

    solid_state_drive_brand = forms.CharField(label='Бренд', max_length=30,
                                              required=True,
                                              help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                              widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    solid_state_drive_model = forms.CharField(label='Модель', max_length=30,
                                              required=True,
                                              help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                              localize=True,
                                              widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    solid_state_drive_memory_size = forms.IntegerField(label='Обсяг пам\'яті', localize=True, required=True,
                                                       help_text='Обов’язково, вказувати в GB',
                                                       widget=widgets.TextInput(
                                                           attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = SolidStateDrive
        fields = ['solid_state_drive_serial_number', 'solid_state_drive_brand', 'solid_state_drive_model',
                  'solid_state_drive_memory_size']


class AddHardDiskDriveForm(forms.ModelForm):
    hard_disk_drive_serial_number = forms.CharField(label='Серійний номер', max_length=30,
                                                    required=True, localize=True,
                                                    help_text='Обов’язково',
                                                    error_messages={
                                                        'unique': 'Жорсткий магнітний диск з таким серійним номером вже існує.'},
                                                    widget=widgets.TextInput(
                                                        attrs={'size': 1, 'class': 'form-control'}))

    hard_disk_drive_brand = forms.CharField(label='Бренд', max_length=30,
                                            required=True,
                                            help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                            widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    hard_disk_drive_model = forms.CharField(label='Модель', max_length=30,
                                            required=True,
                                            help_text='Обов’язково, у разі відсутності - вказати відсутньо',
                                            localize=True,
                                            widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    hard_disk_drive_memory_size = forms.IntegerField(label='Обсяг пам\'яті', localize=True, required=True,
                                                     help_text='Обов’язково, вказувати в GB',
                                                     widget=widgets.TextInput(
                                                         attrs={'size': 1, 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'hard_disk_drive_serial_number',
            'hard_disk_drive_brand',
            'hard_disk_drive_model',
            'hard_disk_drive_memory_size',
            Submit('submit', 'Створити')
        )

    class Meta:
        model = HardDiskDrive
        fields = ['hard_disk_drive_serial_number', 'hard_disk_drive_brand', 'hard_disk_drive_model',
                  'hard_disk_drive_memory_size']


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

    optical_drive_type_drive = forms.ChoiceField(label='Тип оптичного привода', choices=TYPE_OPTICAL_DRIVE,
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


class AddWorkReport(forms.ModelForm):
    inventory_number_pc = forms.CharField(label='Інвентарний номер персонального комп\'ютера', max_length=30,
                                          required=True, help_text='Обов’язково', localize=True,
                                          widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    work_report_field = forms.CharField(label='Опис проведених робіт', help_text='Обов’язково',
                                        localize=True, required=True,
                                        widget=forms.Textarea(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = WorkReport
        fields = ['inventory_number_pc', 'work_report_field']
