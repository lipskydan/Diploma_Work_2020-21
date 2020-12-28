from django.db import models


class PC(models.Model):
    __tablename__ = 'PC'

    inventory_number = models.CharField('інвентарний номер', max_length=200)
    floor = models.IntegerField('номер поверху')
    room = models.IntegerField('номер кабінету')

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