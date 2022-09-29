#!/usr/bin/python3
import atheris
from io import BytesIO
from contextlib import contextmanager
import logging
import sys

with atheris.instrument_imports():
    import cle

# No logging
logging.disable(logging.CRITICAL)


# Disable stdout
@contextmanager
def nostdout():
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = BytesIO()
    sys.stderr = BytesIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr


@atheris.instrument_func
def TestOneInput(data):
    with nostdout():
        try:
            cle.Loader(BytesIO(data), auto_load_libs=False)
        except cle.CLEError:
            pass  # Don't want to report handled exceptions as crashes


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
