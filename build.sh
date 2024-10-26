#!/usr/bin/bash
pyinstaller -F gui.py
rm -rf ./build/
rm -rf gui.spec
mv dist/gui ./GeradorDocs
rm -rf dist