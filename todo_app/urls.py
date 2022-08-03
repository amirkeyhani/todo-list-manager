from django.urls import path

from .views import *

urlpatterns = [
    path('', TodoListView.as_view(), name='index'), 
    path('list/<int:list_id>/', TodoItemListview.as_view(), name='list'), 
    # CRUD patterns for ToDoLists
    path('list/add/', TodoCreateView.as_view(), name='list-add'),
    path('list/<int:pk>/delete/', TodoListDeleteView.as_view(), name='list-delete'),
    # CRUD patterns for ToDoItems
    path('list/<int:list_id>/item/add/', TodoItemCreateView.as_view(), name='item-add'),
    path('list/<int:list_id>/item/<int:pk>/', TodoItemUpdateView.as_view(), name='item-update'), 
    path('list/<int:list_id>/item/<int:pk>/delete/', TodoItemDeleteView.as_view(), name='list-delete'),
]
