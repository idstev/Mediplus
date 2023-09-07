from django.contrib import admin
from .models import Social
# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')
admin.site.register(Social)
