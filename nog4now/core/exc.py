"""nog4now exception classes."""

class nog4nowError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class nog4nowConfigError(nog4nowError):
    """Config related errors."""
    pass

class nog4nowRuntimeError(nog4nowError):
    """Generic runtime errors."""
    pass

class nog4nowArgumentError(nog4nowError):
    """Argument related errors."""
    pass
