"""Filename helpers for NEPSE symbols.

Most symbols are alphanumeric, but a few debentures contain a forward
slash (e.g. ``GBILD84/85``). A slash cannot be part of a filename, so
their CSVs are stored with an underscore (``GBILD84_85.csv``). Both the
history and daily scrapers normalize symbols through ``file_stem`` before
comparing them with the exchange's symbol strings.
"""

_UNSAFE = {"/": "_", "\\": "_"}


def file_stem(symbol):
    """Return the filesystem-safe CSV stem for a NEPSE symbol."""
    clean = str(symbol).strip().upper()
    for char, replacement in _UNSAFE.items():
        clean = clean.replace(char, replacement)
    return clean
