# Based on https://github.com/pauleveritt/customizing_sphinx/tree/master/tests/integration
# and https://github.com/sphinx-doc/sphinx/issues/7008

# stdlib
import sys
from typing import Tuple

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore
from domdf_python_tools.compat import importlib_metadata
from pytest_regressions.file_regression import FileRegressionFixture  # type: ignore
from sphinx_toolbox.testing import check_html_regression


def test(app):
	# app is a Sphinx application object for default sphinx project (`tests/doc-test/test-root`).
	app.build()


# @pytest.mark.sphinx(buildername='latex')
# def test_latex(app):
# 	# latex builder is chosen here.
# 	app.build()

# pytestmark = pytest.mark.sphinx('html', testroot='root')

docutils_version = tuple(map(int, importlib_metadata.version("docutils").split('.')))[:2]


def _param(version: Tuple[int, int]):

	return pytest.param(
			version,
			marks=pytest.mark.skipif(
					docutils_version != version,
					reason="Difference in output between docutils versions (current version {}.{})".format(
							*docutils_version
							),
					),
			id="{}.{}".format(*version)
			)


lt_38 = pytest.mark.skipif(
		condition=sys.version_info < (3, 8),
		reason="Difference in output between 3.6/3.7 and 3.8+",
		)

gte_38 = pytest.mark.skipif(
		condition=sys.version_info >= (3, 8, 0),
		reason="Difference in output between 3.6/3.7 and 3.8+",
		)


@pytest.mark.parametrize("py_version", [
		pytest.param("37", marks=gte_38),
		pytest.param("38", marks=lt_38),
		])
@pytest.mark.parametrize("docutils_version", [_param((0, 16)), _param((0, 17))])
@pytest.mark.parametrize("page", ["index.html", "string.html", "csv.html"], indirect=True)
def test_page(py_version: str, docutils_version: str, page: BeautifulSoup, file_regression: FileRegressionFixture):
	check_html_regression(page, file_regression)
