from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User


# Create your models here.
class Catagorie(models.Model):
    catagorie_id = models.IntegerField(primary_key=True)
    catagorie_name = models.CharField(max_length=50)

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField()
    location = models.TextField(null=True, blank=True)
    ticket_price = models.IntegerField()
    ticket_amount = models.IntegerField()
    picture = models.ImageField(upload_to='img')
    is_popular = models.BooleanField(default=False)
    catagorie = models.ForeignKey(Catagorie, on_delete=PROTECT)

class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=PROTECT)
    user_id = models.ForeignKey(User, on_delete=PROTECT)
    purchased_date = models.DateField(auto_now=True)

