from django.contrib import admin
from . import models


@admin.register(models.Deploy)
class DeployAdmin(admin.ModelAdmin):
    list_display = ('project', 'stage', 'status')
