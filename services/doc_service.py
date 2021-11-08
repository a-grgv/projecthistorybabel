"""
This module contains methods to interact with SavedDocs stored in the database.
"""

from datetime import datetime
from typing import List, Tuple

from utils.application_factories.database import db
from models.saved_doc import SavedDoc


def create_new_doc(creator_id: int, title: str, doc_summary: str,
                   doc_events: List[Tuple[datetime, str, str]]) -> SavedDoc:
    """
    Creates a new saved document in database
    :param creator_id: User id of creator
    :param title: Title of doc
    :param doc_summary: Summary of doc
    :param doc_events: Events in doc
    :return: SavedDoc object
    """
    saved_doc = SavedDoc(creator_id=creator_id,
                         title=title,
                         doc_summary=doc_summary,
                         doc_events=doc_events)

    db.session.add(saved_doc)
    db.session.commit()

    return saved_doc


def get_doc_by_id_and_user(doc_id: int, user_id: int) -> SavedDoc:
    """
    Gets a SavedDoc by its creator and id
    :param doc_id: SavedDoc id
    :param user_id: Creator id
    :return: SavedDoc object
    """
    return SavedDoc.query.filter_by(creator_id=user_id).filter_by(id=doc_id).one_or_none()


def delete_doc(doc_id: int, user_id: int) -> List[Tuple[int, str, datetime]]:
    """
    Deletes a saved doc and returns remaining docs for user
    :param doc_id: SavedDoc id
    :param user_id: Creator id
    :return: Remaining docs for user
    """
    db.session.query(
        SavedDoc
    ).filter_by(
        creator_id=user_id
    ).filter_by(
        id=doc_id
    ).delete()
    db.session.commit()
    return get_docs_by_user_id(user_id)


def get_docs_by_user_id(user_id: int) -> List[Tuple[int, str, datetime]]:
    """
    Gets all SavedDocs of a user
    :param user_id: Creator id
    :return:  SavedDocs for a user
    """
    return db.session.query(
        SavedDoc.id,
        SavedDoc.title,
        SavedDoc.doc_created_date
    ).filter_by(
        creator_id=user_id
    ).all()
