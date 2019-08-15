from django.contrib import admin

from .models import Version

# Register your models here.

@admin.register(Version)
class DemoAdmin(admin.ModelAdmin):
    pass
