from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('form/', views.employee_form,name = 'employee_insert'),
    path('list/',views.employee_list,name='employee_list'),
    path('delete/<int:id>/',views.employee_delete,name ='employee_delete'),
    path('<int:id>/',views.employee_form,name='employee_update')

]