from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from projects import models as projects_models
from common import models as common_models


class Task(models.Model):
    name = models.CharField(max_length=255)
    times_used = models.PositiveIntegerField(default=1)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return u'{} ({})'.format(self.name, self.times_used)


class Deploy(common_models.TimestampedModel):

    STATUS_IDLE = 1
    STATUS_PROCESSING = 2
    STATUS_COMPLETED = 3

    STATUS_CHOICES = (
        (STATUS_IDLE, _('Idle')),
        (STATUS_PROCESSING, _('Processing')),
        (STATUS_COMPLETED, _('Completed'))
    )

    project = models.ForeignKey(projects_models.Project)
    stage = models.ForeignKey(projects_models.Stage)
    status = models.IntegerField(
        _('Status'),
        choices=STATUS_CHOICES,
        default=STATUS_IDLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    comments = models.TextField()
    output = models.TextField(null=True, blank=True)
    task = models.ForeignKey(Task, null=True)
    configuration = models.TextField(null=True, blank=True)
