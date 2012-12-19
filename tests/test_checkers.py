from django.contrib.auth.models import User
from django.test import TestCase

from mock import Mock

from doorman.checkers import PermissionChecker
from doorman.exceptions import (
    PermissionAlreadyRegistered,
    PermissionNotRegistered,
)

from basicapp.permissions import can_do_stuff


class PermissionCheckerTestCase(TestCase):

    def setUp(self):
        self.checker = PermissionChecker()

    def test_register_when_unregistered(self):
        self.checker.register('perm', can_do_stuff)
        self.assertEqual(self.checker._registry['basicapp.perm'], can_do_stuff)

    def test_register_when_registered(self):
        self.checker._registry['basicapp.perm'] = can_do_stuff
        self.assertRaises(PermissionAlreadyRegistered,
            self.checker.register, 'perm', can_do_stuff)

    def test_unregister_when_registered(self):
        self.checker._registry['basicapp.perm'] = can_do_stuff
        self.checker.unregister('perm', can_do_stuff)
        self.assertNotIn('basicapp.perm', self.checker._registry)

    def test_unregister_when_unregistered(self):
        self.assertRaises(PermissionNotRegistered,
            self.checker.unregister, 'perm', can_do_stuff)

    def test_has_perm_when_unregistered(self):
        user = User()
        self.assertFalse(self.checker.has_perm(user, 'perm'))

    def test_has_perm_when_registered(self):
        user = User()
        obj = Mock()
        test_func = Mock(return_value=True)
        self.checker._registry['perm'] = test_func
        self.assertTrue(self.checker.has_perm(user, 'perm', obj))
        test_func.assert_called_with(user, obj)

    def test_get_lookup(self):
        lookup = self.checker.get_lookup('perm', can_do_stuff)
        self.assertEqual(lookup, 'basicapp.perm')
