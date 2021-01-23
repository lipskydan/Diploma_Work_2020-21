from django.urls import path
from django.conf.urls import url
from django.urls import re_path

from . import views

from .views import GeneratePDF

app_name = 'IT_items'
urlpatterns = [
    # url(r'^$', views.IT_items, name='IT_items'),
    # url(r'^add-item/$', views.add_item, name='add_item'),
    # url(r'^<str:item_name>/<int:item_id>/$', views.item_detail, name='item_detail'),
    # url(r'^<str:item_name>/<int:item_id>/del/$', views.item_delete, name='item_delete'),
    # url(r'^<str:item_name>/<int:item_id>/update/$', views.item_update, name='item_update'),
    # url(r'^add-item/add-pc/$', views.add_pc, name='add_pc'),

    path('', views.IT_items, name='IT_items'),
    path('pc_accessories', views.pc_accessories, name='pc_accessories'),

    path('add-item', views.add_item, name='add_item'),
    path('add-item/add-pc', views.add_pc, name='add_pc'),
    path('add-item/add-motherboard', views.add_motherboard, name='add_motherboard'),
    path('add-item/add-power-supply', views.add_power_supply, name='add_power_supply'),
    path('add-item/add-video-card', views.add_video_card, name='add_video_card'),
    path('add-item/add-lan-card', views.add_lan_card, name='add_lan_card'),
    path('add-item/add-sound-card', views.add_sound_card, name='add_sound_card'),

    path('<str:item_name>/<int:item_id>', views.item_detail, name='item_detail'),
    path('pc_accessories/<str:item_name>/<int:item_id>', views.pc_accessories_detail, name='item_detail'),

    path('<str:item_name>/<int:item_id>/del', views.item_delete, name='item_delete'),
    path('pc_accessories/<str:item_name>/<int:item_id>/del', views.pc_accessories_delete, name='item_delete'),

    # path('pc_accessories/<str:item_name>/<int:item_id>/del-motherboard', views.motherboard_delete, name='motherboard_delete'),
    # path('pc_accessories/<str:item_name>/<int:item_id>/del-power-supply', views.power_supply_delete, name='power_supply_delete'),
    # path('pc_accessories/<str:item_name>/<int:item_id>/del-video-card', views.video_card_delete, name='video_card_delete'),
    # path('pc_accessories/<str:item_name>/<int:item_id>/del-lan-card', views.lan_card_delete, name='lan_card_delete'),
    # path('pc_accessories/<str:item_name>/<int:item_id>/del-sound-card', views.sound_card_delete, name='sound_card_delete'),

    path('<str:item_name>/<int:item_id>/update-pc', views.pc_update, name='pc_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-motherboard', views.motherboard_update,
         name='motherboard_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-power-supply', views.power_supply_update,
         name='power_supply_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-video-card', views.video_card_update,
         name='video_card_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-lan-card', views.lan_card_update,
         name='lan_card_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-sound-card', views.sound_card_update,
         name='sound_card_update'),

    path('<str:item_name>/<int:item_id>/pdf', GeneratePDF.as_view()),
]
