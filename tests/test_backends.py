from django.contrib.auth.models import User
from django.test import TestCase

from mock import Mock

from doorman.backends import PermissionBackend


class PermissionBackendTestCase(TestCase):

    def setUp(self):
        self.backend = PermissionBackend()
        self.backend.permissions = Mock()

    def test_inactive_user_does_not_have_permission(self):
        user = User(is_active=False)
        self.assertFalse(self.backend.has_perm(user, 'perm'))

    def test_delegates_permission_checks_to_the_checker(self):
        user = User()
        obj = Mock()
        self.backend.has_perm(user, 'perm', obj=obj)
        self.backend.permissions.has_perm.assert_called_with(user, 'perm', obj)

    def test_authenticate_is_not_supported(self):
        self.assertIsNone(self.backend.authenticate())
        self.assertIsNone(self.backend.authenticate('user', 'pass'))
        self.assertIsNone(self.backend.authenticate(u='user', p='pass'))
