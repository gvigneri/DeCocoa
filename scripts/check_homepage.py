"""Compatibility entry point; local-site checks supersede homepage-only checks."""
from check_site import run
if __name__ == '__main__':
    run()
