"""
This module contains the model object for saved documents.
"""

import datetime
from typing import List, Tuple

import pytz as pytz
from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY

from utils.application_factories.database import db


class SavedDoc(db.Model):
    """
    Postgres model for Saved Document
    """
    __tablename__ = 'saved_docs'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id'))
    title = Column(Text, nullable=False)
    doc_summary = Column(Text, nullable=False)
    doc_events = Column(ARRAY(Text))
    doc_created_date = Column(TIMESTAMP(timezone=False), default=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))

    def __init__(self, creator_id: int, title: str, doc_summary: str, doc_events: List[Tuple[datetime, str, str]]):
        self.creator_id = creator_id
        self.title = title
        self.doc_summary = doc_summary
        self.doc_events = doc_events
