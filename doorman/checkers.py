import sys

from doorman.exceptions import (
    PermissionAlreadyRegistered,
    PermissionNotRegistered,
)


class PermissionChecker(object):

    def __init__(self):
        self._registry = {}

    def register(self, perm, test_func):
        """
        Registers the given perm with given test function. If
        the perm has already been registered this will raise
        a PermissionAlreadyRegistered exception.

        """
        lookup = self.get_lookup(perm, test_func)

        if lookup in self._registry:
            raise PermissionAlreadyRegistered('The permission "%s" is '
                'already registered.' % lookup)

        self._registry[lookup] = test_func

    def unregister(self, perm, test_func):
        """
        Un-registers the given perm and test function. If the perm has
        not beed registered this will raise a PermissionNotRegistered
        exception.

        """
        lookup = self.get_lookup(perm, test_func)

        if lookup not in self._registry:
            raise PermissionNotRegistered('The permission "%s" is not been '
                'registered.' % lookup)

        del self._registry[lookup]

    def has_perm(self, user_obj, perm, obj=None):
        """
        Finds the given permissions test function and calls it with the
        given user and object. If the permission has not been registered
        this will return False.

        """
        if perm not in self._registry:
            return False

        return self._registry[perm](user_obj, obj)

    def get_lookup(self, perm, test_func):
        """
        Helper function that determines the lookup for the perm. This
        uses sys.modules incase the function is imported from some other
        location.

        """
        module = sys.modules[test_func.__module__]
        app_label = module.__name__.split('.')[-2]
        return '%s.%s' % (app_label, perm)


permissions = PermissionChecker()
