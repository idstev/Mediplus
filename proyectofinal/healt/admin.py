from django.contrib import admin
from . models import Healt,Atencion
# Register your models here.

class AtencionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Atencion)

class HealtAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    search_fields=('title',)
admin.site.register(Healt)

