from flask import Blueprint, request, redirect, render_template
# from app.app import db
from models import db
from models.entry import Entry


entry_bp = Blueprint('entry', __name__)

# PREFIX = "/entry"

# CREATE ---------------------------------------
@entry_bp.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return True

# GET ALL ---------------------------------------
@entry_bp.route('/')
@entry_bp.route('/index')
def index():
    entries = Entry.query.all()
    return entries 

# UPDATE ---------------------------------------
@entry_bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            title = form.get('title')
            description = form.get('description')
            entry.title = title
            entry.description = description
            db.session.commit()
        return redirect('/')
    return True

# DELETE ---------------------------------------
@entry_bp.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return True

# ERROR HANDLER ---------------------------------------
# @entry_bp.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"
