#!/usr/bin/env python3
"""
Enhanced Sphinx TocTree that shows classes and functions as if they were sections.

:copyright: Copyright (c) 2020 by Dominic Davis-Foster <dominic@davis-foster.co.uk>
:license: BSD, see LICENSE for details.
"""

# stdlib
import os
from pprint import pprint
from typing import Any, Dict, List, Optional, Type, TypeVar

# 3rd party
from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment.adapters.toctree import TocTree
from sphinx.environment.collectors.toctree import TocTreeCollector
from sphinx.transforms import SphinxContentsFilter
from sphinx.util import logging

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"

__license__: str = "BSD"
__version__: str = "0.0.3"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["TocTreePlusCollector", "setup"]

# For type hinting install docutils-stubs

N = TypeVar('N')

logger = logging.getLogger(__name__)

# Used to print information about types not currently enabled.
TOCTREE_PLUS_DEBUG = os.environ.get("TOCTREE_PLUS_DEBUG", 0)


class TocTreePlusCollector(TocTreeCollector):
	"""
	Subclass of :class:`sphinx.environment.collectors.toctree.TocTreePlusCollector`
	that includes classes and functions in the toctree as if they were sections.

	.. TODO:: Nested functions, classes and methods

	"""

	def process_doc(self, app: Sphinx, doctree: nodes.document) -> None:
		"""
		Build a TOC from the doctree and store it in the inventory.

		:param app:
		:param doctree:
		"""

		docname = app.env.docname
		numentries = [0]  # nonlocal again...

		def traverse_in_section(node: nodes.Element, cls: "Type[N]") -> List[N]:
			"""
			Like traverse(), but stay within the same section.

			:param node:
			:param cls:

			:return:
			"""

			result: List[N] = []

			if isinstance(node, cls):
				result.append(node)

			for child in node.children:
				if isinstance(child, nodes.section):
					continue
				elif isinstance(child, nodes.Element):
					result.extend(traverse_in_section(child, cls))

			return result

		def build_toc(node: nodes.Element, depth: int = 1) -> Optional[nodes.bullet_list]:
			"""

			:param node:
			:param depth:

			:return:
			"""

			entries: List[nodes.Element] = []
			item: nodes.Element

			for sectionnode in node:
				# find all toctree nodes in this section and add them
				# to the toc (just copying the toctree node which is then
				# resolved in self.get_and_resolve_doctree)

				if isinstance(sectionnode, nodes.section):
					title = sectionnode[0]
					# copy the contents of the section title, but without references
					# and unnecessary stuff
					visitor = SphinxContentsFilter(doctree)
					title.walkabout(visitor)
					nodetext = visitor.get_entry_text()

					if not numentries[0]:
						# for the very first toc entry, don't add an anchor
						# as it is the file's title anyway
						anchorname = ''
					else:
						anchorname = '#' + sectionnode['ids'][0]

					numentries[0] += 1

					# make these nodes:
					# list_item -> compact_paragraph -> reference
					reference = nodes.reference(
							'',
							'',
							internal=True,
							refuri=docname,
							anchorname=anchorname,
							*nodetext,
							)

					para = addnodes.compact_paragraph('', '', reference)
					item = nodes.list_item('', para)
					sub_item = build_toc(sectionnode, depth + 1)

					if sub_item:
						item += sub_item

					entries.append(item)

				elif isinstance(sectionnode, addnodes.desc):
					# Add class, function and method directives to toctree.
					# (doesn't currently work for method directives - are they nested?)

					if sectionnode.attributes["objtype"] in set(app.env.config.toctree_plus_types):
						attributes = sectionnode.children[0].attributes  # type: ignore

						title = attributes.get("fullname", sectionnode.children[0].astext())
						anchorname = '#' + attributes["ids"][0]

						reference = nodes.reference(
								'',
								'',
								internal=True,
								refuri=docname,
								anchorname=anchorname,
								*[nodes.literal(text=title)],  # type: ignore
								)
						para = addnodes.compact_paragraph('', '', reference)
						item = nodes.list_item('', para)

						entries.append(item)
					elif TOCTREE_PLUS_DEBUG:
						print(sectionnode)
						pprint(sectionnode.attributes["objtype"])

				elif isinstance(sectionnode, addnodes.only):
					onlynode = addnodes.only(expr=sectionnode['expr'])
					blist = build_toc(sectionnode, depth)
					if blist:
						onlynode += blist.children
						entries.append(onlynode)

				elif isinstance(sectionnode, nodes.Element):
					for toctreenode in traverse_in_section(sectionnode, addnodes.toctree):
						item = toctreenode.copy()
						entries.append(item)

						# important: do the inventory stuff
						TocTree(app.env).note(docname, toctreenode)

			if entries:
				return nodes.bullet_list('', *entries)
			else:
				return None

		toc = build_toc(doctree)

		if toc:
			app.env.tocs[docname] = toc
		else:
			app.env.tocs[docname] = nodes.bullet_list('')

		app.env.toc_num_entries[docname] = numentries[0]


def setup(app: Sphinx) -> Dict[str, Any]:
	"""
	Setup Sphinx Extension.

	:param app:

	:return:
	"""

	# Set of types to add to toctree
	app.add_config_value('toctree_plus_types', {"class", "function", "method"}, 'env')
	app.add_env_collector(TocTreePlusCollector)

	return {
			"version": __version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}
