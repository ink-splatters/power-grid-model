# SPDX-FileCopyrightText: 2022 Contributors to the Power Grid Model project <dynamic.grid.calculation@alliander.com>
#
# SPDX-License-Identifier: MPL-2.0

# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "power-grid-model"
copyright = "2022, alliander-opensource"
author = "alliander-opensource"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "numpydoc",
    "hoverxref.extension",
    "myst_nb",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

exclude_patterns = [
    "*/.ipynb_checkpoints/*",
]

# -- myst parser config ------------------------------------------------------
# label references for depth of headers: label name in anchor slug structure
myst_heading_anchors = 3

# -- hoverxref config --------------------------------------------------------
# hover tooltip on python classes
# hoverx links are in sphinx style: {ref} `docs_path\file:Exact Section Name`
hoverxref_domains = [
    "py",
]
hoverxref_default_type = "tooltip"
hoverxref_role_types = {
    "hoverxref": "tooltip",
    "ref": "modal",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "mod": "tooltip",  # for Python Sphinx Domain
    "class": "tooltip",  # for Python Sphinx Domain
    "obj": "tooltip",
    "function": "tooltip",
}

# -- sphinx.autodoc config ---------------------------------------------------
autodoc_default_options = {
    "members": None,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": False,
    "exclude-members": "__weakref__",
}

# -- sphinx.autosectionlabel config -------------------------------------------
autosectionlabel_prefix_document = True

# -- myst_parser or myst_nb -------------------------------------------------
# markdown links [](relative_path\file.ext#section-in-slug)
myst_heading_anchors = 3