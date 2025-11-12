"""
Module: utils.py
Purpose: Helper utilities for cleaning and logging.
"""

import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def pretty_print(title, content):
    print("="*80)
    print(title)
    print("="*80)
    print(content)
    print("="*80)
