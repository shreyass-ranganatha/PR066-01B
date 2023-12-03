#!/usr/bin/env python3

import argparse
import sys
import os


SUPPORTED_FORMATS = {".png", ".jpeg", ".jpg"}


def iterfiles(root: str = "."):
    """generator for identified image files in the `root` tree"""

    for path, ds, fs in os.walk(root):
        for f in fs:
            if os.path.splitext(f)[1] in SUPPORTED_FORMATS:
                yield (path, f)


def main(argv=sys.argv):
    # ap = argparse.ArgumentParser()

    for p, f in iterfiles():
        print(os.path.join(p, f))


if __name__ == '__main__':
    main()
