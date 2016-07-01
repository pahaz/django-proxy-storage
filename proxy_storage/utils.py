# -*- coding: utf-8 -*-
import os


def clean_path(path):
    return os.path.normpath(os.path.join('/', path))
