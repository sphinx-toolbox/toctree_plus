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
	  - |travis| |actions_windows| |actions_macos| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/toctree_plus/latest?logo=read-the-docs
	:target: https://toctree_plus.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/toctree_plus/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/toctree_plus/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/toctree_plus/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/toctree_plus
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/toctree_plus/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/toctree_plus/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/toctree_plus/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/toctree_plus/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/toctree_plus/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/toctree_plus/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/toctree_plus?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/toctree_plus
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

.. |license| image:: https://img.shields.io/github/license/domdfcoding/toctree_plus
	:target: https://github.com/domdfcoding/toctree_plus/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/toctree_plus
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/toctree_plus/v0.0.2
	:target: https://github.com/domdfcoding/toctree_plus/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/toctree_plus
	:target: https://github.com/domdfcoding/toctree_plus/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields

Installation
--------------

.. start installation

``toctree_plus`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install toctree_plus

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
