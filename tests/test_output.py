# Based on https://github.com/pauleveritt/customizing_sphinx/tree/master/tests/integration
# and https://github.com/sphinx-doc/sphinx/issues/7008

# stdlib
import re
import sys
from typing import Tuple

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore
from domdf_python_tools.compat import importlib_metadata
from domdf_python_tools.paths import PathPlus
from sphinx.application import Sphinx
from sphinx_toolbox.testing import HTMLRegressionFixture, LaTeXRegressionFixture


def test(app: Sphinx) -> None:
	# app is a Sphinx application object for default sphinx project (`tests/doc-test/test-root`).
	app.build()


# @pytest.mark.sphinx(buildername='latex')
# def test_latex(app):
# 	# latex builder is chosen here.
# 	app.build()

# pytestmark = pytest.mark.sphinx('html', testroot='root')

docutils_version = tuple(map(int, importlib_metadata.version("docutils").split('.')))[:2]


def _param(version: Tuple[int, int]):  # noqa: MAN002

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
def test_page(py_version: str, docutils_version: str, page: BeautifulSoup, html_regression: HTMLRegressionFixture):

	if page.filename == "csv.html":
		for div in page.select("dt em.sig-param span.n"):
			if div.text in {"new_limit", "dialect", "name", "**fmtparams"}:
				div.replace_with(div.text)
	if page.filename == "string.html":
		for div in page.select("dt em.sig-param span.n"):
			if div.text in {"**kwds", "format_string", "*args", '/'}:
				div.replace_with(div.text)
		# for div in page.select("em.sig-param span.o, em.sig-param span.n"):
		# 	if div.text in {"/", "*args", "**kwargs"}:
		# 		div.replace_with(div.text)

	html_regression.check(page, jinja2=True)


@pytest.mark.parametrize("py_version", [
		pytest.param("37", marks=gte_38),
		pytest.param("38", marks=lt_38),
		])
@pytest.mark.sphinx("latex", srcdir="test-root")
def test_latex_output(app: Sphinx, py_version: str, latex_regression: LaTeXRegressionFixture):

	assert app.builder is not None

	assert app.builder.name.lower() == "latex"

	app.build()

	output_file = PathPlus(app.outdir) / "python.tex"
	content = str(output_file.read_text()).replace("\\sphinxAtStartPar\n", '').replace(". %\n", ".\n")
	content = re.sub(
			r"\\sphinxstepexplicit %\n(\\begin{footnote}\[1])\\phantomsection\\label{\\thesphinxscope\.1}%\n\\sphinxAtStartFootnote",
			"\n\\1\\\\sphinxAtStartFootnote",
			content,
			)

	latex_regression.check(content, jinja2=True)
