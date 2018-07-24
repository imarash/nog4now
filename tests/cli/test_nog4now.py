"""CLI tests for nog4now."""

from nog4now.utils import test

class CliTestCase(test.nog4nowTestCase):
    def test_nog4now_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
