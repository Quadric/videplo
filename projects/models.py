from django.db import models
from django.utils.translation import ugettext as _
from common import models as common_models
from hosts import models as hosts_models



class Project(common_models.TimestampedModel):
    name = models.CharField(_('Name'), max_length=254)
    description = models.TextField(_('Name'), blank=True, null=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name


class Stage(common_models.TimestampedModel):
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('Stage')
        verbose_name_plural = _('Stages')

    def __str__(self):
        return self.name


class HostConfig(common_models.TimestampedModel):
    stage = models.ForeignKey(Stage, verbose_name=_('Stage'))
    host = models.ForeignKey(hosts_models.Host, verbose_name=('Host'))
    ssh_config = models.ForeignKey(hosts_models.SSHConfig, verbose_name=_('SSH Config'))
    is_active = models.BooleanField(_('Is active'))
