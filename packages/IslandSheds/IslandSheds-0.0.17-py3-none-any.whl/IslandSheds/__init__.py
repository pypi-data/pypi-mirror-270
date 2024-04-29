import sys
from importlib.metadata import version, PackageNotFoundError
import inspect
from .downloader import *

_display_details = True

def configure(display_details=True):
    """Configure whether to display function details."""
    global _display_details
    _display_details = display_details

def display_function_details():
    """Displays the names and docstrings of all functions in downloader.py."""
    if _display_details:
        functions_list = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
        for name, func in functions_list:
            if func.__module__.endswith('downloader'):
                print(f"Function: {name}\nDocstring:\n{func.__doc__}\n")

try:
    __version__ = version('islandsheds')  # Replace 'islandsheds' with your actual package name
except PackageNotFoundError:
    __version__ = 'unknown'

display_function_details()