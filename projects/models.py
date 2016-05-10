from django.db import models
from django.utils.translation import ugettext as _


class Project(models.Model):
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name


class Stage(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    name = models.CharField(_('Name'), max_length=254)

    class Meta:
        verbose_name = _('Stage')
        verbose_name_plural = _('Stages')

    def __str__(self):
        return self.name


class Server(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    stage = models.ForeignKey(Stage, verbose_name=_('Stage'))
    name = models.CharField(_('Name'), max_length=254)
    address = models.CharField(_('Hostname/IP'), max_length=254)

    class Meta:
        verbose_name = _('Server')
        verbose_name_plural = _('Servers')

    def __str__(self):
        return '%s (%s)' % (self.name, self.address)