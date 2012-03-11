import os
import sys


def fetch_python_location(buildout):
    """ Determine Python installation location and expose it as buildout variable python-location """

    python = os.path.dirname(sys.executable)
    buildout._raw["buildout"]["python-location"] = os.path.abspath(os.path.join(python, ".."))

    # find the last site-packages path
    for path in sys.path:
        if path.endswith('site-packages'):
            buildout._raw["buildout"]["site-packages"] = path

