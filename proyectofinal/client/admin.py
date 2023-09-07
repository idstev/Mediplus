from django.contrib import admin
from .models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Client, ClientAdmin)




