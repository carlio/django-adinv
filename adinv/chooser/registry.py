registered_choosers = {}


def get_chooser(name):
    return registered_choosers.get(name, None)