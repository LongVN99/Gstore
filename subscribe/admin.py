from django.contrib import admin

# Register your models here.
from .models import SubscribeUser

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_time')

admin.site.register(SubscribeUser, SubscribeAdmin)