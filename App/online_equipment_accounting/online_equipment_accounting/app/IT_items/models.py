from django.db import models

# MOTHERBOARD_CHOICES = [
#     ('', ''),
#     ('ASUS', 'ASUS'),
#     ('ASROCK', 'ASROCK'),
# ]


class Motherboard(models.Model):
    __tablename__ = 'Motherboard'

    # model = models.CharField('модель материнської плати', max_length=200, default='відсутній', choices=MOTHERBOARD_CHOICES)

    model = models.CharField('модель материнської плати', max_length=200, default='відсутній')
    serial_number = models.CharField('серійний номер', max_length=200, default='відсутній')

    name_for_user = 'Материнська плата'
    name = 'Motherboard'

    object = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.model) + ' - серійний номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Материнська плата'
        verbose_name_plural = 'Материнські плати'


class PC(models.Model):
    __tablename__ = 'PC'

    inventory_number = models.CharField('інвентарний номер', max_length=200)
    floor = models.IntegerField('номер поверху')
    room = models.IntegerField('номер кабінету')

    # motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, default='відсутній')
    MOTHERBOARD_CHOICES=Motherboard.object.all()
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)

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