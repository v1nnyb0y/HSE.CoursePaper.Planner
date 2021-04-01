#!/bin/sh
find | grep __pycache__ | xargs rm -rfd
find | grep .pyc | xargs rm -rfd