class PermissionBackend(object):
    """
    Checks permissions using the given permission checkers.

    """
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def __init__(self, checker=None):
        self.checker = checker

    def has_perm(self, user_obj, perm, obj=None):
        if not user_obj.is_active:
            return False
        return self.checker.has_perm(user_obj, perm, obj)

    def authenticate(self, *args, **kwargs):
        # This backend does not support authenticate.
        return None
