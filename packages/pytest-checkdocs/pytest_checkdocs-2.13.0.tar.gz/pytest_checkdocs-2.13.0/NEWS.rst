v2.13.0
=======

Features
--------

- Updated collection to prefer 'file_path' over 'path'. (#23)


v2.12.0
=======

Features
--------

- Rely on jaraco.packaging.metadata for loading metadata. (#19)


v2.11.0
=======

Features
--------

- Bumped dependency on build and removed now unnecessary compatibility wrapper.


v2.10.1
=======

No significant changes.


v2.10.0
=======

Features
--------

- Require Python 3.8 or later.


v2.9.0
======

Prefer ``importlib.metadata`` on Python 3.10 and later.

v2.8.1
======

In README, present badge/link to the docs.

v2.8.0
======

* #17: Prefer `build <https://pypi.org/project/build>`_
  for loading metadata.

v2.7.1
======

* #14: Suppress warnings in tomli (pypa/pep517#122).

v2.7.0
======

* Rely on importlib_metadata 4 to return clean metadata.
  Fixes #10 by eliminating that functionality.

v2.6.0
======

* When dedenting a long description, avoid dedenting if
  not needed, as found in experimental versions of
  ``importlib_metadata``.

v2.5.0
======

#9: Now CheckdocsItem is a simple item and is discovered if
any Python project file (``pyproject.toml``, ``setup.cfg``,
``setup.py``) is found. Also fixes #8.

v2.4.0
======

Rely on `pep517 <https://pypi.org/project/pep517>`_ to load
project metadata. Avoids issue where other stray metadata
might be lying around. Improves support for projects built
by other tools.

v2.3.0
======

Refreshed package. Now ``pytest_checkdocs`` is a package
instead of a module.

v1.2.5
======

Restore compatibility with Python 2.7.

v1.2.4
======

#3: Backport workaround for deprecation warning (now an error).

v2.2.0
======

Added degenerate support for markdown in the check.

v2.1.1
======

Feed mypy hobgoblins.

v2.1.0
======

#3: Add workaround for deprecation warning.
#4: Only require importlib_metadata on older Pythons.

v2.0.0
======

Require Python 3.6 or later.

v1.2.3
======

Rely on docutils 0.15 to include fix for
`docutils 348 <https://sourceforge.net/p/docutils/bugs/348/>`_.

v1.2.2
======

#2: Workaround for ValueError when running under Python 3.8.

v1.2.1
======

#1: Fix issue when run against importlib_metadata 0.21.

v1.2.0
======

Rely on importlib_metadata 0.8 to find local distribution.

Add hacky workaround for when package uses 'src' package layout. See
`importlib_metadata 42 <https://gitlab.com/python-devs/importlib_metadata/issues/42>`_
for more details.

v1.1.1
======

Fix package metadata to include the module.

v1.1.0
======

Instead of invoking setup.py, rely on
`importlib_metadata <https://pypi.org/project/importlib_metadata>`_
to load the long description.

v1.0.0
======

Initial implementation.
