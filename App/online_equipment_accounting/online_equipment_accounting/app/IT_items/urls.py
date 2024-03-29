from django.urls import path
from django.conf.urls import url
from django.urls import re_path

from . import views

from .views import GeneratePDF, GenerateWorkReportPDF

app_name = 'IT_items'
urlpatterns = [

    path('', views.IT_items, name='IT_items'),
    path('pc_accessories', views.pc_accessories, name='pc_accessories'),


    path('add', views.add, name='add'),
    path('add-item/add-pc', views.add_pc, name='add_pc'),
    path('add-item/add-motherboard', views.add_motherboard, name='add_motherboard'),
    path('add-item/add-power-supply', views.add_power_supply, name='add_power_supply'),
    path('add-item/add-video-card', views.add_video_card, name='add_video_card'),
    path('add-item/add-lan-card', views.add_lan_card, name='add_lan_card'),
    path('add-item/add-sound-card', views.add_sound_card, name='add_sound_card'),
    path('add-item/add-optical-drive', views.add_optical_drive, name='add_optical_drive'),
    path('add-item/add-solid-state-drive', views.add_solid_state_drive, name='add_solid_state_drive'),
    path('add-item/add-hard-disk-drive', views.add_hard_disk_drive, name='add_hard_disk_drive'),


    path('<str:item_name>/<int:item_id>', views.item_detail, name='item_detail'),
    path('pc_accessories/<str:item_name>/<int:item_id>', views.pc_accessories_detail, name='item_detail'),

    path('<str:item_name>/<int:item_id>/del', views.item_delete, name='item_delete'),
    path('pc_accessories/<str:item_name>/<int:item_id>/del', views.pc_accessories_delete, name='item_delete'),

    path('<str:item_name>/<int:item_id>/update-pc', views.pc_update, name='pc_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-motherboard', views.motherboard_update,
         name='motherboard_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-solid-state-drive', views.solid_state_drive_update,
         name='solid_state_drive_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-hard-disk-drive', views.hard_disk_drive_update,
         name='hard_disk_drive_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-power-supply', views.power_supply_update,
         name='power_supply_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-video-card', views.video_card_update,
         name='video_card_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-lan-card', views.lan_card_update,
         name='lan_card_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-sound-card', views.sound_card_update,
         name='sound_card_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-optical-drive', views.optical_drive_update,
         name='optical_drive_update'),


    path('<str:item_name>/<int:item_id>/add_work_report', views.add_work_report, name='add_work_report'),
    path('<str:item_name>/<int:item_id>/work_reports', views.work_reports, name='work_reports'),
    path('<str:item_name>/<int:item_id>/work_reports/<str:inventory_number_pc>/<int:report_id>', views.work_report_detail, name='work_report_detail'),
    path('<str:item_name>/<int:item_id>/work_reports/<str:inventory_number_pc>/<int:report_id>/del', views.work_report_del, name='work_report_del'),

    path('error', views.error, name='error'),
    path('<str:item_name>/<int:item_id>/pdf', GeneratePDF.as_view()),
    path('<str:item_name>/<int:item_id>/work_reports/<str:inventory_number_pc>/<int:report_id>/pdf', GenerateWorkReportPDF.as_view()),
]
