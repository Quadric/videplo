from django.contrib import admin
from django.http import JsonResponse

from . import models
from .utils import tail


@admin.register(models.Deploy)
class DeployAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('deploys/css/deploys.css',)
        }
        js = ('deploys/js/deploys.js',)

    list_display = ('project', 'stage', 'status')

    suit_form_includes = (
        ('deploys/admin/console_log_handler.html',),
    )


def read_log_diff(request, log_name, start_byte):
    try:
        log_file = open('deploys/logs/%s' % log_name)
    except FileNotFoundError:
        return JsonResponse({'content': 'console log does not exists'})
    if start_byte == 0:
        tailed = tail(log_file, 500)
        response = {
            'content': tailed[0],
            'end_byte': tailed[1]
        }
    else:
        log_file.seek(start_byte, 0)
        response = {
            'content': log_file.read(),
            'end_byte': log_file.tell()
        }

    return JsonResponse(response)
