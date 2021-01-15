from django.contrib import admin

from .models import PC, Motherboard, PowerSupply, VideoCard

admin.site.register(PC)
admin.site.register(Motherboard)
admin.site.register(PowerSupply)
admin.site.register(VideoCard)