from doorman import permissions


def can_do_stuff(*args, **kwargs):
    return True


permissions.register('can_do_stuff', can_do_stuff)


def can_do_other_stuff(*args, **kwargs):
    return True
