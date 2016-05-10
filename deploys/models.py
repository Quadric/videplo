from django.db import models
from django.utils.translation import ugettext as _
from projects import models as projects_models


class Deploy(models.Model):

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
    status = models.IntegerField(_('Status'), choices=STATUS_CHOICES)
