#!/usr/bin/env python
# help.py
from rich.markdown import Markdown
from macromancer.utils import console

with open("README.md") as readme:
    markdown = Markdown(readme.read())
console.print(markdown)
