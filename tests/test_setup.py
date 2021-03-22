# stdlib
from typing import Iterable

# 3rd party
from sphinx_toolbox.testing import Sphinx, run_setup

# this package
import sphinxcontrib.toctree_plus
from sphinxcontrib.toctree_plus import __version__


def test_setup():

	app: Sphinx
	setup_ret, directives, roles, additional_nodes, app = run_setup(sphinxcontrib.toctree_plus.setup)

	assert setup_ret == {
			"version": __version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}

	assert app.config.values["toctree_plus_types"] == ({"class", "function", "method"}, "env", [Iterable[str]])
