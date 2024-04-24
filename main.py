import sys
from loguru import logger
logger.add(sys.stdout, format='<lvl>{level}</> {message}')
from emotion.ui import init_ui

def main():
    init_ui()

if __name__ == '__main__':
    main()
