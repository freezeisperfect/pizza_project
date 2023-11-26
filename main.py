"""
Main программы. Также возможен запуск из директории modules,
входной точкой там будет cli.py.

Usage
-----
    $ python main.py order margherita --delivery --size XL
    $ python main.py menu
"""
from modules.cli import cli


if __name__ == '__main__':
    cli.main()
