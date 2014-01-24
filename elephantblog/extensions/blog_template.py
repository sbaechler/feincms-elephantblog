# coding: utf-8

"""
    Detail Template Extension
    -------------------------

    This extension allows you to set the detail template. Create a setting
    called BLOG_TEMPLATE_CHOICES like this::

        BLOG_TEMPLATE_CHOICES = (('elephantblog/entry_detail.html', 'Entry'),
                                ('elephantblog/agenda_detail.html', 'Agenda'))

    Keep in mind that the templates only work for detail pages.

"""


from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms import extensions

class Extension(extensions.Extension):

    if not hasattr(settings, 'BLOG_TEMPLATE_CHOICES'):
        raise ImproperlyConfigured('Settings has no BLOG_TEMPLATE_CHOICES')

    def handle_model(self):
        self.model.add_to_class('template_name', models.CharField(_('Template'),
                                max_length=40,
                                choices=settings.BLOG_TEMPLATE_CHOICES,
                                default=settings.BLOG_TEMPLATE_CHOICES[0][0]))

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options(_('Template'), {
            'fields': ('template_name',),
        })