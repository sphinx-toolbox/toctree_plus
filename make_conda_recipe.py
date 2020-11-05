#!/usr/bin/python3

# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import pathlib

# this package
from __pkginfo__ import __version__

description_block = """Enhanced Sphinx TocTree that shows classes and functions as if they were sections.



Before installing please ensure you have added the following channels: domdfcoding, conda-forge
""".replace('"', '\\"')


repo_root = pathlib.Path(__file__).parent
recipe_dir = repo_root / "conda"

if not recipe_dir.exists():
	recipe_dir.mkdir()

all_requirements = (repo_root / "requirements.txt").read_text(encoding="utf-8").split('\n')

# TODO: entry_points, manifest

for requires in {'all': []}.values():
	all_requirements += requires

all_requirements = {x.replace(" ", '') for x in set(all_requirements)}
requirements_block = "\n".join(f"    - {req}" for req in all_requirements if req)

(recipe_dir / "meta.yaml").write_text(
		encoding="UTF-8",
		data=f"""\
package:
  name: "toctree_plus"
  version: "{__version__}"

source:
  url: "https://pypi.io/packages/source/t/toctree_plus/toctree_plus-{__version__}.tar.gz"

build:
  noarch: python
  script: "{{{{ PYTHON }}}} -m pip install . -vv"

requirements:
  build:
    - python
    - setuptools
    - wheel
  host:
    - pip
    - python
{requirements_block}
  run:
    - python
{requirements_block}

test:
  imports:
    - sphinxcontrib.toctree_plus

about:
  home: "https://github.com/domdfcoding/toctree_plus"
  license: "BSD License"
  # license_family: LGPL
  # license_file: LICENSE
  summary: "Enhanced Sphinx TocTree that shows classes and functions as if they were sections."
  description: "{description_block}"
  doc_url: https://toctree_plus.readthedocs.io
  dev_url: https://github.com/domdfcoding/toctree_plus

extra:
  maintainers:
    - Dominic Davis-Foster
    - github.com/domdfcoding

""")

print(f"Wrote recipe to {recipe_dir / 'meta.yaml'}")
