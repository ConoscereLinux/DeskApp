"""Modulo main dell'applicazione."""

# Standard Import
import sys

# Site-package Import

# Project Import
from app import application as a


if __name__ == '__main__':
    sys.exit(a.main(sys.argv))