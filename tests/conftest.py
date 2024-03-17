# stdlib
import pathlib
import sys
from typing import Iterator

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore[import-untyped]
from sphinx.application import Sphinx
from sphinx.testing.path import path

pytest_plugins = ("sphinx.testing.fixtures", "sphinx_toolbox.testing", "coincidence")

if sys.version_info >= (3, 10):
	# stdlib
	import types
	types.Union = types.UnionType


@pytest.fixture(scope="session")
def rootdir() -> path:
	rdir = pathlib.Path(__file__).parent.absolute() / "doc-test"
	if not (rdir / "test-root").is_dir():
		(rdir / "test-root").mkdir(parents=True)
	return path(rdir)


@pytest.fixture()
def content(app: Sphinx) -> Iterator[Sphinx]:
	app.build()
	yield app


@pytest.fixture()
def page(content, request) -> BeautifulSoup:  # noqa: MAN001
	pagename = request.param
	c = (content.outdir / pagename).read_text()

	soup = BeautifulSoup(c, "html5lib")
	soup.filename = pagename

	yield soup
