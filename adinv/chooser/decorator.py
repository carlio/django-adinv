from django.core.exceptions import ImproperlyConfigured

registered_choosers = {}


def chooser(name=None):
    name_or_function = name # used to make the keyword argument nicer
    
    if name_or_function is None:
        # this was used like '@chooser()'
        # this means that we don't have a name argument, but we also don't have
        # the function to get a name from... boo. we'd have to call the value
        # we have to get the actual function decorated, but this could (although
        # shouldn't) have side effects... therefore we can only defer registering
        # the chooser until it's actualy used, which means it won't show up in the
        # admin interface for example. This sucks, so we'll jsut throw a wobbly and
        # tell the user they can't used the decorator like this.
        raise ImproperlyConfigured('chooser decorator requires a name argument, or to be used without calling')
        
    elif callable(name_or_function):
        # this was used like '@chooser', so the argument
        # is a function
        func_name = name_or_function.__name__
        func = name_or_function
    
    else:
        # this was used like '@chooser("fish")'
        func_name = name_or_function
        def dec(func):
            print func
            return func
        func = dec
    
    registered_choosers[func_name] = func
    return func