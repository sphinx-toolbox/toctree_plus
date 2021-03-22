================
.. toctree:: +
================

.. start short_desc

**Enhanced Sphinx TocTree that shows classes and functions as if they were sections.**

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
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/toctree_plus/latest?logo=read-the-docs
	:target: https://toctree_plus.readthedocs.io/en/latest
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

.. |requires| image:: https://requires.io/github/sphinx-toolbox/toctree_plus/requirements.svg?branch=master
	:target: https://requires.io/github/sphinx-toolbox/toctree_plus/requirements/?branch=master
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/toctree_plus/v0.2.0
	:target: https://github.com/sphinx-toolbox/toctree_plus/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/toctree_plus
	:target: https://github.com/sphinx-toolbox/toctree_plus/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/toctree_plus
	:target: https://pypi.org/project/toctree_plus/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/sphinx-toolbox/toctree_plus/master.svg
	:target: https://results.pre-commit.ci/latest/github/sphinx-toolbox/toctree_plus/master
	:alt: pre-commit.ci status

.. end shields

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

		$ conda config --add channels http://conda.anaconda.org/conda-forge
		$ conda config --add channels http://conda.anaconda.org/domdfcoding

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

- Source: https://github.com/domdfcoding/toctree_plus
- Bugs: https://github.com/domdfcoding/toctree_plus/issues
