from django.contrib import admin
from . import models
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user


class StageInline(admin.StackedInline):
    model = models.Stage

#
# class ServerInline(admin.StackedInline):
#     model = models.Server


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StageInline]


@admin.register(models.Stage)
class StageAdmin(admin.ModelAdmin):
    # inlines = [ServerInline]
    pass


# @admin.register(models.Server)
# class ServerAdmin(GuardedModelAdmin):
#
#     list_display = ('name', 'address', 'ping')
#
#     def get_queryset(self, request):
#         return get_objects_for_user(request.user, 'projects.change_server')
#
#     def ping(self, value):
#         """
#         Returns True if host responds to a ping request
#         """
#         import os, platform
#
#         # Ping parameters as function of OS
#         ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
#
#         # Ping
#         return os.system("ping " + ping_str + " " + value.address) == 0
#     ping.short_description = 'Online'
#     ping.boolean = True


@admin.register(models.Host)
class HostAdmin(GuardedModelAdmin):

    list_display = ('name', 'alias', 'ping')
    #
    # def get_queryset(self, request):
    #     return get_objects_for_user(request.user, 'projects.change_server')

    def ping(self, value):
        """
        Returns True if host responds to a ping request
        """
        import os, platform

        # Ping parameters as function of OS
        ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

        # Ping
        return os.system("ping " + ping_str + " " + value.name) == 0
    ping.short_description = 'Online'
    ping.boolean = True
