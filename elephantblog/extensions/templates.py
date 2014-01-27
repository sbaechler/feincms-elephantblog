# coding: utf-8
""" This extensions adds the template selector to the admin."""

from feincms import extensions
from django.utils.translation import ugettext_lazy as _


class Extension(extensions.Extension):
    def handle_model(self):
        pass

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options(_('Template'), {
            'fields': ('template_key',),
        })