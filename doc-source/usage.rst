======
Usage
======


Installation
--------------

.. start installation

.. installation:: toctree_plus
	:pypi:
	:github:
	:anaconda:
	:conda-channels: conda-forge, domdfcoding

.. end installation


.. raw:: latex


	\bigskip\bigskip\hrule\bigskip


.. extensions:: toctree_plus
	:import-name: sphinxcontrib.toctree_plus

Configuration
--------------

.. confval:: toctree_plus_types
	:type: :class:`~typing.Dict`\[:class:`str`\]
	:default: ``{"class", "function", "method"}``

	This determines the directive types that appear in the toctree.
