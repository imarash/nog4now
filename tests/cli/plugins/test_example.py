"""Tests for Example Plugin."""

from nog4now.utils import test

class ExamplePluginTestCase(test.nog4nowTestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
