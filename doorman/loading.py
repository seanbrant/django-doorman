import copy

from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule

from doorman import permissions


def autodiscover():
    """
    Auto-discover INSTALLED_APPS permissions.py modules and fail silenty when
    not present. This forces an import on them to register any permission
    checks they may want.

    """
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)

        # Attempt to import the app's permissions module.
        try:
            before_import_registry = copy.copy(permissions._registry)
            import_module('%s.permissions' % app)
        except:
            # Roll back the registry to prevent NotRegistered and
            # AlreadyRegistered exceptions
            permissions._registry = before_import_registry

            # Not bubble up the error if the app does not have
            # a permissions module.
            if module_has_submodule(mod, 'permissions'):
                raise
