from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'time')

admin.site.register(Message, MessageAdmin)