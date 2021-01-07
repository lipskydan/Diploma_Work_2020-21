from django.db import models

MOTHERBOARD_FROM_FACTORS = [
    ('не вказано', ''),
    ('ATX', 'ATX'),
    ('microATX', 'microATX'),
    ('Mini-ITX', 'Mini-ITX'),
    ('Nano-ITX', 'Nano-ITX'),
    ('Pico-ITX', 'Pico-ITX'),
]

TYPE_RAM_SLOTS = [
    ('не вказано', ''),
    ('DIMM', 'DIMM'),
    ('RIMM', 'RIMM'),
    ('DDR DIMM', 'DDR DIMM'),
    ('DDR2', 'DDR2'),
    ('DDR3', 'DDR3'),
]


class Motherboard(models.Model):
    __tablename__ = 'Motherboard'

    brand = models.CharField('бренд материнської плати', max_length=200, default='відсутній')
    model = models.CharField('модель материнської плати', max_length=200, default='відсутній')

    serial_number = models.CharField('серійний номер', max_length=200, unique=False)

    form_factor = models.CharField(max_length=20, choices=MOTHERBOARD_FROM_FACTORS)
    type_ram_slot = models.CharField(max_length=20, choices=TYPE_RAM_SLOTS)

    integrated_graphics = models.BooleanField(default=False)
    integrated_sound_card = models.BooleanField(default=False)
    integrated_lan_card = models.BooleanField(default=False)

    # is_established = models.BooleanField(default=False)

    name_for_user = 'Материнська плата'
    name = 'Motherboard'

    object = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Материнська плата'
        verbose_name_plural = 'Материнські плати'


class PowerSupply(models.Model):
    __tablename__ = 'PowerSupply'

    brand = models.CharField('бренд блока живлення', max_length=200, default='відсутній')
    model = models.CharField('модель блока живлення', max_length=200, default='відсутній')

    serial_or_inventory_number = models.CharField('серійний або інвентарний номер',
                                                  max_length=200, unique=True, default='відсутній')

    power_consumption = models.IntegerField('споживана потужність')

    name_for_user = 'Блок живлення'
    name = 'PowerSupply'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_or_inventory_number)

    class Meta:
        verbose_name = 'Блок живлення'
        verbose_name_plural = 'Блоки живлення'


class PC(models.Model):
    __tablename__ = 'PC'

    inventory_number = models.CharField('інвентарний номер', max_length=200, unique=True)

    floor = models.IntegerField('номер поверху')
    room = models.IntegerField('номер кабінету')
    place = models.IntegerField('номер учбового місця', default=0, blank=True, null=True)

    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.SET_NULL, null=True)

    name_for_user = 'Персональний комп\'ютор'
    name = 'PC'

    objects = models.Manager()

    def __str__(self):
        return self.name + ' - поверх ' + str(self.floor) + ' - кабінет ' + str(self.room) + ' - ' + str(
            self.inventory_number)

    class Meta:
        verbose_name = 'Персональний комп\'ютор'
        verbose_name_plural = 'Персональні комп\'ютори'
