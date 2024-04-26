"""
Antigranular client package
"""


from .client import login
from .client import read_config
from .client import write_config
from .client import load_config
# Package version dunder
__version__ = "1.0.1"

# Package author dunder
__author__ = "Oblivious Software Pvt. Ltd."

# Package * imports dunder
__all__ = ["login", "read_config", "write_config", "load_config", "__version__", "__author__"]

# Read default config on import
# try:
#     read_config()
# except Exception:
#     pass # Ignore if config file is not found