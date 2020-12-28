from django import forms


class AddPcForm(forms.Form):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True)
    floor = forms.IntegerField(label='Номер поверху', required=True, help_text='Обов’язково',
                               localize=True)
    room = forms.IntegerField(label='Номер кабінету', required=True, help_text='Обов’язково',
                              localize=True)

