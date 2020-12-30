from django import forms

from .models import Motherboard, PC


class AddPcForm(forms.ModelForm):
    inventory_number = forms.CharField(label='Інвентарний номер', max_length=30, required=True, help_text='Обов’язково',
                                       localize=True)
    floor = forms.IntegerField(label='Номер поверху', required=True, help_text='Обов’язково',
                               localize=True)
    room = forms.IntegerField(label='Номер кабінету', required=True, help_text='Обов’язково',
                              localize=True)

    # motherboard_model = forms.CharField(label='Модель материнської плати', max_length=30, required=False,
    #                                     help_text='Необов’язково',
    #                                     localize=True,
    #                                     widget=forms.Select(choices=MOTHERBOARD_CHOICES, attrs={'style': 'width: 175px; height: 29px'}),)

    motherboard = forms.ModelChoiceField(queryset=Motherboard.object.all(), label='Материнська плата',
                                         empty_label='', required=False, help_text='Необов’язково',
                                         localize=True, )



    # motherboard_model.widget.attrs.update(size='1.5')

    # motherboard_serial_number = forms.CharField(label='Серійний номер материнської плати', max_length=30,
    #                                             required=False, help_text='Необов’язково',
    #                                             localize=True)


    class Meta:
        model = PC
        fields = ['inventory_number', 'floor', 'room', 'motherboard', ]

        widgets = {
            'motherboard': forms.Select(attrs={'class': 'form-control'})
        }