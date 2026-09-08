#!/usr/bin/env python
"""Django administrative utility."""

import os
import sys


def main() -> None:
    """Run Django management commands."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django is unavailable. Install project dependencies before running manage.py."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
