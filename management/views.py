from builtins import object
from datetime import date
from venv import create

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from management.models import Event, Ticket


# Create your views here.
def payment(request,id_event):
    event = Event.objects.filter(event_id=id_event)
    dict = {
            'id': event[0].event_id,
            'name': event[0].event_name,
            'number': request.GET['number'],
            'price':event[0].ticket_price,
            'date':date.today(),
            'amount':range(event[0].ticket_amount+1),
            'total': int(request.GET['number'])*event[0].ticket_price,
            'ticket_id': (Ticket.objects.all().count() + 1)
        }
    
    return render(request, template_name='payment.html',context=dict)

def create_ticket(request,user_id,number):
    id_event = request.POST.get('id')
    event = Event.objects.get(pk=id_event)
    event.ticket_amount = (event.ticket_amount-number)
    event.save()
    user = User.objects.get(pk=user_id)
    for n in range(number):
        amount = (Ticket.objects.all().count() + 1)
        ticket = Ticket(ticket_id=amount,event_id=event,user_id=user)
        ticket.save()
    return redirect('homepage')

def payment_regis(request,number):
    user = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
    user.first_name = request.POST.get('firstname')
    user.last_name = request.POST.get('lastname')
    user.save()
    
    id_event = request.POST.get('id')
    event = Event.objects.get(pk=id_event)
    event.ticket_amount = (event.ticket_amount-number)
    event.save()
    for n in range(number):
        amount = (Ticket.objects.all().count() + 1)
        ticket = Ticket(ticket_id=amount,event_id=event,user_id=user)
        ticket.save()
    return redirect('homepage')