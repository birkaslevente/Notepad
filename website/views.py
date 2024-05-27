from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required

def home():
    user_emails = []  # Declare and initialize the user_emails list outside of the if statement
    # fill user_emails with the emails of all users except the current user
    users = User.query.all()
    for user in users:
        if user.email != current_user.email:
            user_emails.append(user.email)
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user, user_emails=user_emails)

@views.route('/hu', methods=['GET', 'POST'])
def hu():
    user_emails = []  # Declare and initialize the user_emails list outside of the if statement
    # fill user_emails with the emails of all users except the current user
    users = User.query.all()
    for user in users:
        if user.email != current_user.email:
            user_emails.append(user.email)
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home_hu.html', user=current_user, user_emails=user_emails)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})
#write a share function, that will allow users to share notes with other users
@views.route('/share-note', methods=['POST'])
@views.route('/share-note', methods=['POST'])
def share_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    email = data['email']
    
    # Megkeressük az user_id-t az email cím alapján
    user = User.query.filter_by(email=email).first()
    
    if user:
        # Ha találunk felhasználót az adott email címmel
        note = Note.query.get(noteId)
        if note:
            # Megkeressük a jegyzetet az id alapján és átadjuk a data-t
            new_note = Note(data=note.data, user_id=user.id)
            db.session.add(new_note)
            db.session.commit()
            return jsonify({'message': 'A jegyzet sikeresen megosztva.'})
        else:
            return jsonify({'error': 'A jegyzet nem található.'})
    else:
        # Ha nem találunk felhasználót az adott email címmel
        return jsonify({'error': 'Nem található felhasználó az adott email címmel.'})