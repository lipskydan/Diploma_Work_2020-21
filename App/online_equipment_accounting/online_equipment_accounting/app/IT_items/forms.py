from django import forms


class AddPcForm(forms.Form):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True)
    floor = forms.IntegerField(label='Номер поверху', required=True, help_text='Обов’язково',
                               localize=True)
    room = forms.IntegerField(label='Номер кабінету', required=True, help_text='Обов’язково',
                              localize=True)

    motherboard_model = forms.CharField(label='Модель материнської плати', max_length=30, required=False,
                                        help_text='Необов’язково',
                                        localize=True)
    motherboard_serial_number = forms.CharField(label='Серійний номер материнської плати', max_length=30,
                                                required=False, help_text='Необов’язково',
                                                localize=True)
