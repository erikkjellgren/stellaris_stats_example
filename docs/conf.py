#!/usr/bin/env python3

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = ""
copyright = ""
author = ""

# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes"]

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {"preamble": r"\pdfimageresolution=144"}
latex_documents = [
    (master_doc, "sphinx-example.tex", "sphinx-example Documentation", "Firstname Lastname", "manual",)
]

# -- Options for manual page output ---------------------------------------
man_pages = [(master_doc, "sphinx-example", "sphinx-example Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    (
        master_doc,
        "sphinx-example",
        "sphinx-example Documentation",
        author,
        "sphinx-example",
        "One line description of project.",
        "Miscellaneous",
    ),
]
