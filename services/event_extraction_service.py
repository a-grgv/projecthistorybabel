import spacy
import re
from daterangeparser import parse

p = re.compile(r'\[\d+\]')
nlp = spacy.load("en_core_web_sm")


def dep_subtree(token, dep):
    child = next(filter(lambda c: c.dep_ == dep, token.children), None)
    if child is not None:
        return " ".join([c.text for c in child.subtree])
    else:
        return ""


def extract_events_spacy(line):
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


def extract_all_events(text):
    all_events = []

    # Process the events
    for processed, line in enumerate(text.splitlines()):
        events = extract_events_spacy(line)
        all_events = all_events + events
    return all_events
