================
.. toctree:: +
================

.. start short_desc

.. documentation-summary::

.. end short_desc

.. start shields

.. only:: html

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

	.. |docs| rtfd-shield::
		:project: toctree_plus
		:alt: Documentation Build Status

	.. |docs_check| actions-shield::
		:workflow: Docs Check
		:alt: Docs Check Status

	.. |actions_linux| actions-shield::
		:workflow: Linux
		:alt: Linux Test Status

	.. |actions_windows| actions-shield::
		:workflow: Windows
		:alt: Windows Test Status

	.. |actions_macos| actions-shield::
		:workflow: macOS
		:alt: macOS Test Status

	.. |actions_flake8| actions-shield::
		:workflow: Flake8
		:alt: Flake8 Status

	.. |actions_mypy| actions-shield::
		:workflow: mypy
		:alt: mypy status

	.. |requires| requires-io-shield::
		:alt: Requirements Status

	.. |coveralls| coveralls-shield::
		:alt: Coverage

	.. |codefactor| codefactor-shield::
		:alt: CodeFactor Grade

	.. |pypi-version| pypi-shield::
		:project: toctree_plus
		:version:
		:alt: PyPI - Package Version

	.. |supported-versions| pypi-shield::
		:project: toctree_plus
		:py-versions:
		:alt: PyPI - Supported Python Versions

	.. |supported-implementations| pypi-shield::
		:project: toctree_plus
		:implementations:
		:alt: PyPI - Supported Implementations

	.. |wheel| pypi-shield::
		:project: toctree_plus
		:wheel:
		:alt: PyPI - Wheel

	.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/toctree_plus?logo=anaconda
		:target: https://anaconda.org/domdfcoding/toctree_plus
		:alt: Conda - Package Version

	.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/toctree_plus?label=conda%7Cplatform
		:target: https://anaconda.org/domdfcoding/toctree_plus
		:alt: Conda - Platform

	.. |license| github-shield::
		:license:
		:alt: License

	.. |language| github-shield::
		:top-language:
		:alt: GitHub top language

	.. |commits-since| github-shield::
		:commits-since: v0.2.2
		:alt: GitHub commits since tagged version

	.. |commits-latest| github-shield::
		:last-commit:
		:alt: GitHub last commit

	.. |maintained| maintained-shield:: 2021
		:alt: Maintenance

	.. |pypi-downloads| pypi-shield::
		:project: toctree_plus
		:downloads: month
		:alt: PyPI - Downloads

.. end shields

This idea has been suggested in :issue:`6316 <sphinx-doc/sphinx>` and :issue:`6435 <sphinx-doc/sphinx>`.

You can see ``toctree-plus`` in action in `this project's documentation`_,
and the documentation for domdf-python-tools_ (ReadTheDocs Sphinx Theme) and whey_ (Furo Sphinx Theme).

.. _this project's documentation: https://toctree-plus.readthedocs.io/en/latest/docs.html
.. _domdf-python-tools: https://domdf-python-tools.readthedocs.io/en/latest/api/iterative.html
.. _whey: https://whey.readthedocs.io/en/latest/api/config.html


Contents
-----------

.. html-section::


.. toctree::
	:hidden:

	Home<self>


.. toctree::
	:maxdepth: 3

	usage
	Demo<demo>
	api
	Source


.. toctree::
        :caption: Links
        :hidden:

        GitHub <https://github.com/sphinx-toolbox/toctree_plus>
        PyPI <https://pypi.org/project/toctree_plus>
        Contributing Guide <https://contributing-to-sphinx-toolbox.readthedocs.io/en/latest/>


.. start links

.. only:: html

	View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

	`Browse the GitHub Repository <https://github.com/sphinx-toolbox/toctree_plus>`__

.. end links
