#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as runserver

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_core.settings')

    # Alterar Porta default do Servidor Django `runserver` command
    runserver.default_port = os.getenv("DJ_SERVER")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))