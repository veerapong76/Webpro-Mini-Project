
import datetime
from asyncio import events
from builtins import object
from re import search
from urllib import request
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from e_ticket import urls
from management.models import Event, Ticket,Catagorie


def homepage(request):
    event = Event.objects.filter(event_date__gte=datetime.date.today())
    list = []
    list2 =[]
    for ev in event[0:5]:
        dict = {
            'id':ev.event_id,
            'name':ev.event_name,
            'date':ev.event_date,
            'price':ev.ticket_price,
            'picture':ev.picture,
            'location':ev.location,
        }
        list.append(dict)

    catagorie = Catagorie.objects.all()
    for c in catagorie[0:5]:
        dict = {
            'id':c.catagorie_id,
            'name':c.catagorie_name,
        }
        list2.append(dict)
    
    return render(request, template_name='home.html',context={
        'event': list,
        'catagorie':list2,
        'head':'Popular Right Now'
    })
def my_login(request):
    context = {}
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
        
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'
    
    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def detail(request,id_event):
    event = Event.objects.filter(event_id=id_event)
    dict = {
            'id':event[0].event_id,
            'name':event[0].event_name,
            'date':event[0].event_date,
            'price':event[0].ticket_price,
            'picture':event[0].picture,
            'location':event[0].location,
            'description':event[0].description,
            'range_amount':range(event[0].ticket_amount+1),
            'amount':event[0].ticket_amount,
            'catagorie':event[0].catagorie.catagorie_name
        }
    return render(request, template_name='detail.html', context=dict)


def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        return redirect('login')

    return render(request,template_name='register.html')


def profile(request,id_user):
    ticket = Ticket.objects.filter(user_id=id_user)
    list=[]
    for tk in ticket:
        dict = {
            'ticket_id':tk.ticket_id,
            'event_id':tk.event_id.event_id,
            'event_name':tk.event_id.event_name,
            'event_date':tk.event_id.event_date,
            'description':tk.event_id.description,
            'purchased_date':tk.purchased_date
        }
        list.append(dict)
    
    return render(request,template_name='profile.html' ,context={
        'ticket':list
    })

def search_event(request):
    search_txt = request.GET.get('txt_search')
    event = Event.objects.filter(Q(event_name__icontains=search_txt) | Q(catagorie__catagorie_name__iexact=search_txt))
    list = []
    for ev in event:
        dict = {
            'id':ev.event_id,
            'name':ev.event_name,
            'date':ev.event_date,
            'price':ev.ticket_price,
            'picture':ev.picture,
            'location':ev.location,
        }
        list.append(dict)
    
    return render(request,template_name='home.html',context={
        'event':list,
        'head':'Search Event:',
        'tail':search_txt
    })

def all_event(request):
    event = Event.objects.all()
    list = []
    for ev in event:
        dict = {
            'id':ev.event_id,
            'name':ev.event_name,
            'date':ev.event_date,
            'price':ev.ticket_price,
            'picture':ev.picture,
            'location':ev.location,
        }
        list.append(dict)
    
    return render(request,template_name='home.html',context={
        'event':list,
        'head':'Events:',
    })

def all_catagorie(request):
    list = []
    catagorie = Catagorie.objects.all()
    for c in catagorie:
        dict = {
            'id':c.catagorie_id,
            'name':c.catagorie_name,
        }
        list.append(dict)
    
    return render(request,template_name='home.html',context={
        'catagorie':list,
        'head':'Catagories:',
        
    })

def search_catagorie(request, name):
    event = Event.objects.filter(catagorie__catagorie_name__icontains=name)
    list = []
    for ev in event:
        dict = {
            
            'id':ev.event_id,
            'name':ev.event_name,
            'date':ev.event_date,
            'price':ev.ticket_price,
            'picture':ev.picture,
            'location':ev.location,
        }
        list.append(dict)
    
    return render(request,template_name='home.html',context={
        'event':list,
        'head':'Search Catagorie:',
        'tail':name
    })

def edit_profile(request,id_user):
    if request.method == 'POST':
        user = User.objects.get(pk=id_user)
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.save()
        return redirect('login')
    return render(request,template_name='register.html')

