#!/bin/bash

rm -rf build dist *.egg-info

python3 setup.py sdist bdist_wheel

twine upload dist/*
