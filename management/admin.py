from django.contrib import admin
from management.models import Event,Ticket,Catagorie
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_name', 'event_date','location','ticket_price','ticket_amount','picture','is_popular','catagorie']


admin.site.register(Event,EventAdmin)
admin.site.register(Ticket)
admin.site.register(Catagorie)