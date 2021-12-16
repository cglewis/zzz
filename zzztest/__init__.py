"""
Initialize variables that might be needed anywhere, like the version
"""
from pbr.version import VersionInfo

__version__ = VersionInfo('zzztest').semantic_version().release_string()
