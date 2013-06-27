# coding: utf-8

from django.test.utils import override_settings
import factory
from django.core import management
from django.test.testcases import TestCase
from django.utils import translation
from .factories import EntryFactory, create_entries

from elephantblog.models import Entry
from django.test import Client


class ApplicationContentTest(TestCase):

    def setUp(self):
        create_entries(EntryFactory)