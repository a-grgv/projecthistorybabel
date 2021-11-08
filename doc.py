"""
This module defines endpoints for document interaction
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from forms import DocumentForm
from services import summarization_service, translation_service, event_extraction_service, doc_service
from utils.blueprint_constants import TRANSLATIONS, TEXT, DOC_SUMMARY, DOC_EVENTS

doc = Blueprint('doc', __name__, template_folder='templates/doc')


@doc.route('/create', methods=('POST', 'GET'))
@login_required
def create_doc():
    """
    Create Doc endpoint
    :return:
    """
    form = DocumentForm()
    if request.method == 'POST':
        text = form.article.data
        title = form.title.data
        user_id = current_user.id
        translated_text = translation_service.translate_text(text)[0][TRANSLATIONS][0][TEXT]
        doc_summary = summarization_service.summarize_text(translated_text)
        doc_events = event_extraction_service.extract_all_events(translated_text)
        doc_service.create_new_doc(creator_id=user_id,
                                   title=title,
                                   doc_summary=doc_summary,
                                   doc_events=doc_events)
        return jsonify({
            DOC_SUMMARY: doc_summary,
            DOC_EVENTS: doc_events
        })
    return render_template('create.html', form=form)


@doc.route('/doc/<doc_id>', methods=['GET'])
@login_required
def get_saved_doc(doc_id):
    """
    Get saved doc
    :param doc_id: doc id
    :return:
    """
    user_id = current_user.id
    saved_doc = doc_service.get_doc_by_id_and_user(doc_id, user_id)
    return render_template('saved_doc.html', doc=saved_doc)


@doc.route('/list', methods=('POST', 'GET'))
@login_required
def get_saved_doc_list():
    """
    Get list of saved docs of user
    :return:
    """
    user_id = current_user.id
    doc_list = doc_service.get_docs_by_user_id(user_id=user_id)
    return render_template('doc_list.html', doc_list=doc_list)


@doc.route('/delete-doc/<doc_id>', methods=['GET'])
@login_required
def delete_saved_doc(doc_id):
    """
    Delete a saved document
    :param doc_id: doc id
    :return:
    """
    user_id = current_user.id
    remaining_doc_list = doc_service.delete_doc(user_id=user_id, doc_id=doc_id)
    return render_template('doc_list.html', doc_list=remaining_doc_list)
