"""nog4now bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as nog4nowBaseController.

from nog4now.cli.controllers.base import nog4nowBaseController

def load(app):
    app.handler.register(nog4nowBaseController)
