================
.. toctree:: +
================

.. start short_desc

**Enhanced Sphinx TocTree which shows classes, functions etc. as if they were sections.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/toctree-plus/latest?logo=read-the-docs
	:target: https://toctree-plus.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/Docs%20Check/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/Linux/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/Windows/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/macOS/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/Flake8/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/sphinx-toolbox/toctree_plus/workflows/mypy/badge.svg
	:target: https://github.com/sphinx-toolbox/toctree_plus/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/sphinx-toolbox/toctree_plus/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/sphinx-toolbox/toctree_plus/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/sphinx-toolbox/toctree_plus/master?logo=coveralls
	:target: https://coveralls.io/github/sphinx-toolbox/toctree_plus?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sphinx-toolbox/toctree_plus?logo=codefactor
	:target: https://www.codefactor.io/repository/github/sphinx-toolbox/toctree_plus
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/toctree_plus
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/toctree_plus?logo=python&logoColor=white
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/toctree_plus
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/toctree_plus
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/toctree_plus?logo=anaconda
	:target: https://anaconda.org/domdfcoding/toctree_plus
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/toctree_plus?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/toctree_plus
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/toctree_plus
	:target: https://github.com/sphinx-toolbox/toctree_plus/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/toctree_plus
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/toctree_plus/v0.8.0
	:target: https://github.com/sphinx-toolbox/toctree_plus/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/toctree_plus
	:target: https://github.com/sphinx-toolbox/toctree_plus/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2024
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/toctree_plus
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Downloads

.. end shields

This idea has been suggested in `sphinx-doc/sphinx#6316`_ and `sphinx-doc/sphinx#6435`_

You can see ``toctree-plus`` in action in `this project's documentation`_,
and the documentation for domdf-python-tools_ (ReadTheDocs Sphinx Theme) and whey_ (Furo Sphinx Theme).

.. _sphinx-doc/sphinx#6316: https://github.com/sphinx-doc/sphinx/issues/6316
.. _sphinx-doc/sphinx#6435: https://github.com/sphinx-doc/sphinx/issues/6435
.. _this project's documentation: https://toctree-plus.readthedocs.io/en/latest/docs.html
.. _domdf-python-tools: https://domdf-python-tools.readthedocs.io/en/latest/api/iterative.html
.. _whey: https://whey.readthedocs.io/en/latest/api/config.html

Installation
--------------

.. start installation

``toctree_plus`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install toctree_plus

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install toctree_plus

.. end installation

Enable ``toctree_plus`` by adding ``"sphinxcontrib.toctree_plus"`` to the ``extensions`` variable in ``conf.py``:

.. code-block:: python

	extensions = [
		...
		"sphinxcontrib.toctree_plus",
		]

For more information see https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions .

Configuration
^^^^^^^^^^^^^^^^

There is currently only a single configuration option: ``toctree_plus_types``.
This determines the directive types that appear in the toctree. The default value is ``{"class", "function", "method"}``.

Links
-----

- Source: https://github.com/sphinx-toolbox/toctree_plus
- Bugs: https://github.com/sphinx-toolbox/toctree_plus/issues
