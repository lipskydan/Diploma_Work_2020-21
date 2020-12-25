from django.urls import path
from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'IT_items'

urlpatterns = [
    # url(r'^$', views.IT_items, name='IT_items'),
    # url(r'^add-item/$', views.add_item, name='add_item'),
    # url(r'^<str:item_name>/<int:item_id>/$', views.item_detail, name='item_detail'),
    # url(r'^<str:item_name>/<int:item_id>/del/$', views.item_delete, name='item_delete'),
    # url(r'^<str:item_name>/<int:item_id>/update/$', views.item_update, name='item_update'),
    # url(r'^add-item/add-pc/$', views.add_pc, name='add_pc'),

    path('', views.IT_items, name='IT_items'),
    path('add-item', views.add_item, name='add_item'),
    path('<str:item_name>/<int:item_id>', views.item_detail, name='item_detail'),
    path('<str:item_name>/<int:item_id>/del', views.item_delete, name='item_delete'),
    path('<str:item_name>/<int:item_id>/update', views.item_update, name='item_update'),
    path('add-item/add-pc', views.add_pc, name='add_pc'),
]

