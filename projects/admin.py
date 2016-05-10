from django.contrib import admin
from . import models


class StageInline(admin.StackedInline):
    model = models.Stage


class ServerInline(admin.StackedInline):
    model = models.Server


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StageInline, ServerInline]


@admin.register(models.Stage)
class StageAdmin(admin.ModelAdmin):
    inlines = [ServerInline]


@admin.register(models.Server)
class ServerAdmin(admin.ModelAdmin):

    list_display = ('name', 'address', 'ping')

    def ping(self, value):
        """
        Returns True if host responds to a ping request
        """
        import os, platform

        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

        # Ping
        return os.system("ping " + ping_str + " " + value.address) == 0
    ping.short_description = 'Online'
    ping.boolean = True
