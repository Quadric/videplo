from django.db import models
from django.utils.translation import ugettext as _
from common import models as common_models


class Host(models.Model):
    """Defines a Host that deployments can be made to"""

    name = models.CharField(
        _('Hostname/IP'),
        max_length=254,
        help_text='DNS name or IP address'
    )

    alias = models.CharField(
        _('Human readable name'),
        blank=True,
        null=True,
        max_length=255,
        help_text='Human readable value (optional)',
    )

    class Meta:
        verbose_name = _('Host')
        verbose_name_plural = _('Hosts')

    def __str__(self):
        return self.name


class SSHConfig(models.Model):
    name = models.CharField(_('Name'), max_length=254)
    remote_user = models.CharField(_('Remove User'), max_length=100)
    private_key = models.TextField(_('Private Key'))

    class Meta:
        verbose_name = _('SSHConfig')
        verbose_name_plural = _('SSHConfig')

    def __str__(self):
        return self.name
