"""nog4now main application entry point."""

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from nog4now.core import exc

# Application default.  Should update config/nog4now.conf to reflect any
# changes, or additions here.
defaults = init_defaults('nog4now')

# All internal/external plugin configurations are loaded from here
defaults['nog4now']['plugin_config_dir'] = '/etc/nog4now/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['nog4now']['plugin_dir'] = '/var/lib/nog4now/plugins'

# External templates (generally, do not ship with application code)
defaults['nog4now']['template_dir'] = '/var/lib/nog4now/templates'


class nog4nowApp(CementApp):
    class Meta:
        label = 'nog4now'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'nog4now.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'nog4now.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'nog4now.cli.templates'

        # call sys.exit() when app.close() is called
        exit_on_close = True


class nog4nowTestApp(nog4nowApp):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = nog4nowApp()

def main():
    with app:
        try:
            app.run()
        
        except exc.nog4nowError as e:
            # Catch our application errors and exit 1 (error)
            print('nog4nowError > %s' % e)
            app.exit_code = 1
            
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1
            
        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
