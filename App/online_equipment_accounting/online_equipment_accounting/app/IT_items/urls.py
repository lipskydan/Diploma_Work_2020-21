from django.urls import path
from django.urls import re_path

from . import views

app_name = 'IT_items'

urlpatterns = [
    path('', views.IT_items, name='IT_items'),
    path('add-item', views.add_item, name='add_item'),
    path('<str:item_name>/<int:item_id>', views.item_detail, name='item_detail'),
    path('<str:item_name>/<int:item_id>/del', views.item_delete, name='item_delete'),
    path('<str:item_name>/<int:item_id>/update', views.item_update, name='item_update'),
    path('add-item/add-pc', views.add_pc, name='add_pc'),
]