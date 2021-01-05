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

    path('<str:item_name>/<int:item_id>', views.item_detail, name='item_detail'),
    path('<str:item_name>/<int:item_id>/del', views.item_delete, name='item_delete'),
    path('<str:item_name>/<int:item_id>/update', views.item_update, name='item_update'),

    path('<str:item_name>/<int:item_id>/pdf', GeneratePDF.as_view()),

    path('pc_accessories/<str:item_name>/<int:item_id>', views.pc_accessories_detail, name='item_detail'),
    path('pc_accessories/<str:item_name>/<int:item_id>/del', views.pc_accessories_delete, name='item_delete'),

    path('pc_accessories/<str:item_name>/<int:item_id>/update-motherboard', views.motherboard_update, name='motherboard_update'),
    path('pc_accessories/<str:item_name>/<int:item_id>/update-power-supply', views.power_supply_update, name='power_supply_update'),
]


