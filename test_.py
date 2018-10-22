import os

from settings import ROOT_DIR


def find_path(pkg):
    path = os.path.join(ROOT_DIR, pkg)
    assert os.path.isdir(path), 'Directory not found at {}'.format(pkg)
    return path
