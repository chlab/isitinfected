"""The collect-images command"""

from .base import Base
from json import dumps


class Collect_Images(Base):
    """Collect images from reddit"""

    def run(self):
        print 'Hello, world!'
        print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)