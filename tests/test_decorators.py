from django.test import TestCase

from doorman import permissions, register

from basicapp.permissions import can_do_other_stuff


class RegisterTestCase(TestCase):

    def test_with_no_name(self):
        wrapped = register(can_do_other_stuff)
        self.assertEqual(wrapped, can_do_other_stuff)
        self.assertEqual(
            permissions._registry['basicapp.can_do_other_stuff'],
            can_do_other_stuff,
        )

    def test_with_name(self):
        wrapped = register('perm_name')(can_do_other_stuff)
        self.assertEqual(wrapped, can_do_other_stuff)
        self.assertEqual(
            permissions._registry['basicapp.perm_name'],
            can_do_other_stuff,
        )
