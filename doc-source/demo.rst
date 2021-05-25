====================
.. toctree:: + Demo
====================

.. only:: latex

	.. include:: _blurb.rst

.. note::

	This documentation was generated with the following setting in ``conf.py``:

	.. code-block:: python

		toctree_plus_types = {"class", "function", "data"}

.. attention::

	Observe that the methods of :class:`~.AClass` do not appear in the TOC. This is a known limitation.


.. py:class:: AClass

	.. py:method:: __repr__()

	.. py:method:: __str__()

	.. py:method:: __int__()

	.. py:method:: __float__()

.. py:data:: months
	:annotation: = ['Jan', 'Feb', ...]

.. py:function:: a_function(foo, bar, baz)
