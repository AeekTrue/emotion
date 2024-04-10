import sys
from loguru import logger
logger.add(sys.stdout, format='<lvl>{level}</> {message}')

from emotion.ui import init_ui
from emotion.storage import storage

class Card():
    parent = None
    id_ = None
    def __init__(self, parent=None, properties=None):
        self.properties = properties

def main():
    init_ui()

if __name__ == '__main__':
    main()
