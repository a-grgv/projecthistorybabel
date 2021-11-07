from models.database import db
from models.saved_doc import SavedDoc


def create_new_doc(creator_id, title, doc_summary, doc_events):
    saved_doc = SavedDoc(creator_id=creator_id,
                         title=title,
                         doc_summary=doc_summary,
                         doc_events=doc_events)

    db.session.add(saved_doc)
    db.session.commit()

    return saved_doc


def get_doc_by_id_and_user(doc_id, user_id):
    return SavedDoc.query.filter_by(creator_id=user_id).filter_by(id=doc_id).one_or_none()


def delete_doc(doc_id, user_id):
    db.session.query(
        SavedDoc
    ).filter_by(
        creator_id=user_id
    ).filter_by(
        id=doc_id
    ).delete()
    db.session.commit()
    return get_docs_by_user_id(user_id)


def get_docs_by_user_id(user_id):
    return db.session.query(
        SavedDoc.id,
        SavedDoc.title,
        SavedDoc.doc_created_date
    ).filter_by(
        creator_id=user_id
    ).all()
