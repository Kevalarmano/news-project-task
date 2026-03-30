"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys
import django

# Add the Django project root to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# Tell Django which settings module to use
os.environ['DJANGO_SETTINGS_MODULE'] = 'news_project.settings'

# Initialise Django so autodoc can import models, views, etc.
django.setup()

# -- Project information -------------------------------------------------
project = 'News Project'
copyright = '2026, Keval Armano Ramchander'
author = 'Keval Armano Ramchander'
release = '1.0'

# -- General configuration -----------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
