"""
This module contains methods to extract events from text
"""

from datetime import datetime
from typing import List, Tuple

import spacy
import re
from daterangeparser import parse
from spacy.tokens.token import Token

p = re.compile(r'\[\d+\]')
nlp = spacy.load("en_core_web_sm")


def dep_subtree(token: Token, dep: str) -> str:
    """
    Traverse a dependency subtree
    :param token: Spacy Token
    :param dep: Part of speech
    :return: Text from subtree
    """
    child = next(filter(lambda c: c.dep_ == dep, token.children), None)
    if child is not None:
        return " ".join([c.text for c in child.subtree])
    else:
        return ""


def extract_events_spacy(line: str) -> List[Tuple[datetime, str, str]]:
    """
    Extract events from text
    :param line: Text with events
    :return: List of tuple of extracted date object, textual date and event description
    """
    line = p.sub('', line)
    events = []
    doc = nlp(line)
    for ent in filter(lambda e: e.label_ == 'DATE', doc.ents):
        try:
            start, end = parse(ent.text)
        except:
            # could not parse the dates, hence ignore it
            continue
        current = ent.root
        while current.dep_ != "ROOT":
            current = current.head
        desc = " ".join(filter(None, [
            dep_subtree(current, "nsubj"),
            dep_subtree(current, "nsubjpass"),
            dep_subtree(current, "auxpass"),
            dep_subtree(current, "amod"),
            dep_subtree(current, "det"),
            current.text,
            dep_subtree(current, "acl"),
            dep_subtree(current, "dobj"),
            dep_subtree(current, "attr"),
            dep_subtree(current, "advmod")]))
        events = events + [(start, ent.text, desc)]
    return events


def extract_all_events(text: str) -> List[Tuple[datetime, str, str]]:
    """
    Extract all events from text
    :param text: Text with events
    :return: List of extracted events
    """
    all_events = []

    for processed, line in enumerate(text.splitlines()):
        events = extract_events_spacy(line)
        all_events = all_events + events
    return all_events
