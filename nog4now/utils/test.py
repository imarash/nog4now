"""Testing utilities for nog4now."""

from nog4now.cli.main import nog4nowTestApp
from cement.utils.test import *

class nog4nowTestCase(CementTestCase):
    app_class = nog4nowTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(nog4nowTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(nog4nowTestCase, self).tearDown()

