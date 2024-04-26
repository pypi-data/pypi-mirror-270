import os
import sys


def restart(*argv):
    e = sys.executable
    a = argv or sys.argv
    os.execl(e, e, *a)
