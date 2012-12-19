class PermissionAlreadyRegistered(Exception):
    """
    The permission being registered has already been registered.

    """


class PermissionNotRegistered(Exception):
    """
    The permission being unregistered has not been registered yet.

    """
