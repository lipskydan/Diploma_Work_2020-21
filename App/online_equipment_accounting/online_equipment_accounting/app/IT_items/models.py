from django.db import models

# MOTHERBOARD_CHOICES = [
#     ('', ''),
#     ('ASUS', 'ASUS'),
#     ('ASROCK', 'ASROCK'),
# ]


class Motherboard(models.Model):
    __tablename__ = 'Motherboard'

    brand = models.CharField('бренд материнської плати', max_length=200, default='відсутній')
    model = models.CharField('модель материнської плати', max_length=200, default='відсутній')

    serial_number = models.CharField('серійний номер', max_length=200, unique=True)

    integrated_graphics = models.BooleanField(default=False)
    integrated_sound_card = models.BooleanField(default=False)
    integrated_lan_card = models.BooleanField(default=False)

    # is_established = models.BooleanField(default=False)

    name_for_user = 'Материнська плата'
    name = 'Motherboard'

    object = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - серійний номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Материнська плата'
        verbose_name_plural = 'Материнські плати'


class PC(models.Model):
    __tablename__ = 'PC'

    inventory_number = models.CharField('інвентарний номер', max_length=200, unique=True)

    floor = models.IntegerField('номер поверху')
    room = models.IntegerField('номер кабінету')
    place = models.IntegerField('номер учбового місця', default=0, blank=True, null=True)

    # MOTHERBOARD_CHOICES=Motherboard.object.all()
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True)

    # end = models.DateField(default=None, blank=True, null=True)
    # pub_date = models.DateTimeField('дата створення')
    # b = models.CharField(max_length=7, default="foobar")

    name_for_user = 'Персональний комп\'ютор'
    name = 'PC'

    objects = models.Manager()

    def __str__(self):
        return self.name + ' - поверх ' + str(self.floor) + ' - кабінет ' + str(self.room) + ' - ' + str(self.inventory_number)

    class Meta:
        verbose_name = 'Персональний комп\'ютор'
        verbose_name_plural = 'Персональні комп\'ютори'