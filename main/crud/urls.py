from django.urls import path
from .views import *
urlpatterns = [
    # path('',index,name='index'),
    # path('add/',add,name='add'),
    # path('edit/',edit,name='edit'),
    # path('update/<int:id>',update,name='update'),
    # path('delete/<int:id>',delete,name='delete'),

    # ++++++++++++++++++++anoher method+++++++++++++++++
    path('', EmployeeListView.as_view(), name='index'),
    path('add/', EmployeeCreateView.as_view(), name='add'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='delete'),
    path('delete_selected/', delete_selected, name='delete_selected'),
]
