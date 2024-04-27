#!/usr/bin/env python3

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

from .core import (
	mst, gcd, lcm, ratioSimp, Mat,
	zeros, ones, diag, eye, randmat, hilbert)

__all__ = [
	'mst',
	'gcd',
	'lcm',
	'ratioSimp',
	
	'Mat',
	'zeros',
	'ones',
	'diag',
	'eye',
	'randmat',
	'hilbert',
	
	'__version__',
]
