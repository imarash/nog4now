"""nog4now base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

class nog4nowBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'No Glance For Now (nog4now)'
        arguments = [
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        print("Inside nog4nowBaseController.default().")

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``nog4now.cli.templates``, or ``/var/lib/nog4now/templates/``.
        #
