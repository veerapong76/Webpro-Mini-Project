from venv import create

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('/<int:id_event>', views.payment,name='payment'),
    path('create_ticket/<int:user_id>/<int:number>',views.create_ticket,name='create_ticket'),
    path('payment_regis/<int:number>',views.payment_regis,name='payment_regis'),
]
