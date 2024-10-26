#!/usr/bin/bash
pyinstaller -F src/gui.py
pyinstaller -F src/generate_docs.py
rm -rf ./build/
rm -rf *.spec
mv dist/gui ./GeradorDocs
mv dist/generate_docs ./generate_docs
rm -rf dist