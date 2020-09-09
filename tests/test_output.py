# Based on https://github.com/pauleveritt/customizing_sphinx/tree/master/tests/integration
# and https://github.com/sphinx-doc/sphinx/issues/7008

# stdlib
import sys

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore
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


@pytest.mark.skipif(condition=sys.version_info < (3, 8), reason="Difference in output between 3.6/3.7 and 3.8+")
@pytest.mark.parametrize("page", ["index.html", "string.html", "csv.html"], indirect=True)
def test_page_38(page: BeautifulSoup, file_regression: FileRegressionFixture):
	check_html_regression(page, file_regression)


@pytest.mark.skipif(
		condition=sys.version_info >= (3, 8, 0),
		reason="Difference in output between 3.6/3.7 and 3.8+",
		)
@pytest.mark.parametrize("page", ["index.html", "string.html", "csv.html"], indirect=True)
def test_page_37(page: BeautifulSoup, file_regression: FileRegressionFixture):
	check_html_regression(page, file_regression)
