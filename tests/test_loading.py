import sys

from django.test import TestCase

from doorman import autodiscover, permissions


class AutodiscoverTestCase(TestCase):

    def test_loads_permissions_module_in_app(self):
        del sys.modules['basicapp.permissions']
        permissions._registry = {}
        autodiscover()
        self.assertIn('basicapp.can_do_stuff', permissions._registry)
