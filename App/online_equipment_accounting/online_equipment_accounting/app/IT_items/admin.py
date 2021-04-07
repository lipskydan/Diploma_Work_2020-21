from django.contrib import admin

from .models import PC, Motherboard, PowerSupply, VideoCard, LanCard, SoundCard, OpticalDrive

admin.site.register(PC)
admin.site.register(Motherboard)
admin.site.register(PowerSupply)
admin.site.register(VideoCard)
admin.site.register(LanCard)
admin.site.register(SoundCard)
admin.site.register(OpticalDrive)

