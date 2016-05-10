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
    pass
