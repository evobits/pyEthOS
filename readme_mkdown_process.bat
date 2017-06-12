pandoc --from=markdown --to=rst --output=README.rst README.md
copy /Y README.md docs\index.md
PAUSE;