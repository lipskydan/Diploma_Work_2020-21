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

TYPE_OPTICAL_DRIVE = [
    ('не вказано', ''),
    ('DVD', 'DVD'),
    ('CD', 'CD'),
    ('CD-R', 'CD-R'),
    ('CD-RM', 'CD-RM'),
]

TYPE_CONNECTOR_OF_OPTICAL_DRIVE = [
    ('не вказано', ''),
    ('SATA', 'SATA'),
    ('PATA', 'PATA'),
]

TYPE_OPERATING_SYSTEM = [
    ('не вказано', ''),
    ('Windows 10', 'Windows 10'),
    ('Windows 7', 'Windows 7'),
    ('Windows XP', 'Windows XP'),
    ('Ubuntu', 'Ubuntu'),
]


class Motherboard(models.Model):
    __tablename__ = 'Motherboard'

    brand = models.CharField('бренд материнської плати', max_length=200, default='відсутній')
    model = models.CharField('модель материнської плати', max_length=200, default='відсутній')

    serial_number = models.CharField('серійний номер', max_length=200, unique=True, default='відсутній')

    form_factor = models.CharField(max_length=20, choices=MOTHERBOARD_FROM_FACTORS, default='не вказано')
    type_ram_slot = models.CharField(max_length=20, choices=TYPE_RAM_SLOTS, default='не вказано')

    integrated_graphics = models.BooleanField(default=False)
    integrated_sound_card = models.BooleanField(default=False)
    integrated_lan_card = models.BooleanField(default=False)

    name_for_user = 'Материнська плата'
    name = 'Motherboard'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Материнська плата'
        verbose_name_plural = 'Материнські плати'


class SolidStateDrive(models.Model):
    __tablename__ = 'SolidStateDrive'

    brand = models.CharField('бренд', max_length=200, default='відсутній')
    model = models.CharField('модель', max_length=200, default='відсутній')

    serial_number = models.CharField('серійний номер', max_length=200, unique=True, default='відсутній')
    memory_size = models.IntegerField('обсяг пам\'яті', default=0)

    name_for_user = 'Твердотільний накопичувач'
    name = 'SolidStateDrive'

    objects = models.Manager()

    def __str__(self):
        return str(self.brand) + ' ' + str(self.memory_size) + ' ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Твердотільний накопичувач'
        verbose_name_plural = 'Твердотільні накопичувачі'


class HardDiskDrive(models.Model):
    __tablename__ = 'HardDiskDrive'

    brand = models.CharField('бренд', max_length=200, default='відсутній')
    model = models.CharField('модель', max_length=200, default='відсутній')

    serial_number = models.CharField('серійний номер', max_length=200, unique=True, default='відсутній')
    memory_size = models.IntegerField('обсяг пам\'яті', default=0)

    name_for_user = 'Жорсткий магнітний диск'
    name = 'HardDiskDrive'

    objects = models.Manager()

    def __str__(self):
        return str(self.brand) + ' ' + str(self.memory_size) + ' ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Жорсткий магнітний диск'
        verbose_name_plural = 'Жорсткі магнітні диски'


class PowerSupply(models.Model):
    __tablename__ = 'PowerSupply'

    brand = models.CharField('бренд блока живлення', max_length=200, default='відсутній')
    model = models.CharField('модель блока живлення', max_length=200, default='відсутній')

    serial_or_inventory_number = models.CharField('серійний або інвентарний номер',
                                                  max_length=200, unique=True, default='відсутній')

    power_consumption = models.IntegerField('споживана потужність', default=0)

    name_for_user = 'Блок живлення'
    name = 'PowerSupply'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_or_inventory_number)

    class Meta:
        verbose_name = 'Блок живлення'
        verbose_name_plural = 'Блоки живлення'


class VideoCard(models.Model):
    __tablename__ = 'VideoCard'

    brand = models.CharField('бренд відеокарти', max_length=200, default='відсутній')
    model = models.CharField('модель відеокарти', max_length=200, default='відсутній')
    serial_number = models.CharField('серійний номер', max_length=200, unique=True, default='відсутній')
    memory_size = models.IntegerField('обсяг пам\'яті', default=0)

    name_for_user = 'Відеокарта'
    name = 'VideoCard'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Відеокарта'
        verbose_name_plural = 'Відеокарти'


class LanCard(models.Model):
    __tablename__ = 'LanCard'

    brand = models.CharField('бренд мережевої плати', max_length=200, default='відсутній')
    model = models.CharField('модель мережевої плати', max_length=200, default='відсутній')
    serial_number = models.CharField('серійний номер', max_length=200, unique=True, default='відсутній')

    name_for_user = 'Мережева плата'
    name = 'LanCard'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Мережева плата'
        verbose_name_plural = 'Мережеві плати'


class SoundCard(models.Model):
    __tablename__ = 'SoundCard'

    brand = models.CharField('бренд звукової плати', max_length=200, default='відсутній')
    model = models.CharField('модель звукової плати', max_length=200, default='відсутній')
    serial_number = models.CharField('серійний номер', max_length=200, unique=False, default='відсутній')

    name_for_user = 'Звукова плата'
    name = 'SoundCard'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Звукова плата'
        verbose_name_plural = 'Звукові плати'


class OpticalDrive(models.Model):
    __tablename__ = 'OpticalDrive'

    brand = models.CharField('бренд оптичного накопичувача', max_length=200, default='відсутній')
    model = models.CharField('модель оптичного накопичувача', max_length=200, default='відсутній')
    serial_number = models.CharField('серійний номер', max_length=200, unique=False, default='відсутній')
    type_drive = models.CharField(max_length=20, choices=TYPE_OPTICAL_DRIVE, default='не вказано')
    type_connector = models.CharField(max_length=20, choices=TYPE_CONNECTOR_OF_OPTICAL_DRIVE, default='не вказано')

    name_for_user = 'Оптичний накопичувач'
    name = 'OpticalDrive'

    objects = models.Manager()

    def __str__(self):
        return 'модель ' + str(self.brand) + ' ' + str(self.model) + ' - номер ' + str(self.serial_number)

    class Meta:
        verbose_name = 'Оптичний накопичувач'
        verbose_name_plural = 'Оптичні накопичувачі'


class PC(models.Model):
    __tablename__ = 'PC'

    inventory_number = models.CharField('інвентарний номер', max_length=200, unique=True)

    floor = models.IntegerField('номер поверху')
    room = models.IntegerField('номер кабінету')
    place = models.IntegerField('номер учбового місця', default=0, blank=True, null=False)

    operating_system = models.CharField(max_length=20, choices=TYPE_OPERATING_SYSTEM, default='не вказано')

    motherboard = models.ForeignKey(Motherboard, on_delete=models.OneToOneField, null=True)
    power_supply = models.ForeignKey(PowerSupply, on_delete=models.OneToOneField, null=True)
    video_card = models.ForeignKey(VideoCard, on_delete=models.OneToOneField, null=True)
    lan_card = models.ForeignKey(LanCard, on_delete=models.OneToOneField, null=True)
    sound_card = models.ForeignKey(SoundCard, on_delete=models.OneToOneField, null=True)
    optical_drive = models.ForeignKey(OpticalDrive, on_delete=models.OneToOneField, null=True)

    text_field = models.TextField(default='Місце для нотаток')

    name_for_user = 'Персональний комп\'ютор'
    name = 'PC'

    objects = models.Manager()

    def __str__(self):
        return self.name + ' - поверх ' + str(self.floor) + ' - кабінет ' + str(self.room) + ' - ' + str(
            self.inventory_number)

    class Meta:
        verbose_name = 'Персональний комп\'ютор'
        verbose_name_plural = 'Персональні комп\'ютори'
